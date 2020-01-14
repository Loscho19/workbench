function _sel(sel) {
  return document.querySelector(sel)
}

/* eslint-disable-next-line */
function _cl(el, cl, add) {
  el.classList[add ? "add" : "remove"](cl)
}

$(function() {
  const gettext =
    window.gettext ||
    function(t) {
      return t
    }

  // AJAX modals
  const dismissModals = function() {
    // LOL, dismiss.
    $(".modal, .modal-backdrop").remove()
    $(document.body)
      .removeClass("modal-open")
      .removeAttr("style")
  }

  const initModal = function(data) {
    dismissModals()

    $(data).modal()

    setTimeout(function() {
      const fields = $(".modal").find("input, select")
      if (fields.filter("[autofocus]").length) {
        fields.filter("[autofocus]").focus()
      } else {
        fields
          .filter(":visible")
          .first()
          .focus()
      }
    }, 100)

    initWidgets()
  }

  window.initModal = initModal
  window.openModalFromUrl = function(url) {
    $.ajax({
      url: url,
      success: function(data) {
        initModal(data)
      },
      error: function() {
        alert(gettext("Unable to open the form"))
      },
      xhrFields: {
        withCredentials: true,
      },
    })
  }

  $(document.body).on("click", "[data-toggle]", function(event) {
    if (this.dataset.toggle == "ajaxmodal") {
      event.preventDefault()
      window.openModalFromUrl(this.href)
    }
  })

  $(document.body).on("submit", ".modal-dialog form", function(_event) {
    if (this.method.toLowerCase() == "post") {
      const action = this.action,
        data = $(this).serialize()
      this.parentNode.removeChild(this)
      $.post(action, data, function(data, status, jqXHR) {
        // 201 CREATED, 202 ACCEPTED or 204 NO CONTENT
        if (
          jqXHR.status === 201 ||
          jqXHR.status === 202 ||
          jqXHR.status === 204
        ) {
          $(document).trigger("modalform", [jqXHR.status, action])
          dismissModals()
          window.location.reload()
        } else if (jqXHR.status === 299) {
          window.location.href = data.redirect
        } else {
          initModal(data)
        }
      })
    } else {
      $.get(this.action + "?" + $(this).serialize(), function(
        data /*,
        status,
        jqXHR
        */
      ) {
        initModal(data)
      })
    }
    return false
  })

  // Autosubmit forms
  $(document.body).on(
    "change",
    "form[data-autosubmit] select, form[data-autosubmit] input",
    function() {
      $(this)
        .closest("form")
        .submit()
    }
  )

  // Search form restoration
  $(".form-search").each(function() {
    let params = new URLSearchParams(window.location.search.slice(1))
    ;["page", "pdf", "xlsx", "_error"].forEach(key => params.delete(key))
    params.sort()
    params = params.toString()
    const key = `search-${window.location.pathname}`
    window.localStorage.setItem(key, params ? `?${params}` : "")
  })

  function localStorageKeyFor(href) {
    return `search-${href}`
  }

  function restoreSearch(href) {
    return href + (window.localStorage.getItem(localStorageKeyFor(href)) || "")
  }

  // Restore the search params when going through the main menu...
  $(".navbar").on("click", "a", function(e) {
    const orig = e.originalEvent
    if (orig.altKey || orig.ctrlKey || orig.metakey || orig.shiftKey) return

    e.preventDefault()
    window.location.href = restoreSearch(this.getAttribute("href"))
  })

  $("h1, [data-reset-filter]").on("click", function() {
    window.localStorage.removeItem(localStorageKeyFor(window.location.pathname))
  })

  // Hotkeys
  $(document.body).on("keydown", function(e) {
    if (/Mac/.test(navigator.platform) ? !e.ctrlKey : !e.altKey) {
      return
    }

    if (e.keyCode === 70) {
      // f
      $(".form-search input[name=q]")
        .focus()
        .select()
    } else if (e.keyCode === 72) {
      // h
      window.location.href = "/"
    } else if (e.keyCode === 67 && e.shiftKey) {
      // Shift-c
      window.openModalFromUrl("/contacts/people/select/")
    } else if (e.keyCode === 67) {
      // c
      window.location.href = restoreSearch("/contacts/people/")
    } else if (e.keyCode === 80 && e.shiftKey) {
      // Shift-p
      window.openModalFromUrl("/projects/select/")
    } else if (e.keyCode === 80) {
      // p
      window.location.href = restoreSearch("/projects/")
    } else if (e.keyCode === 79) {
      // o
      window.location.href = restoreSearch("/offers/")
    } else if (e.keyCode === 82) {
      // r
      window.location.href = restoreSearch("/invoices/")
    } else if (e.keyCode === 76) {
      // l
      const el = _sel("[data-createhours]")
      if (e.shiftKey || !el) {
        window.openModalFromUrl("/logbook/hours/create/")
      } else {
        window.openModalFromUrl(el.href)
      }
    } else if (e.keyCode === 75) {
      // k
      const el = _sel("[data-createcost]")
      if (e.shiftKey || !el) {
        window.openModalFromUrl("/logbook/costs/create/")
      } else {
        window.openModalFromUrl(el.href)
      }
    } else if (e.keyCode === 81) {
      // q
      $(".navbar input[type=search]")
        .focus()
        .select()
    } else if (e.keyCode === 13) {
      $(e.target)
        .parents("form")
        .submit()
    } else {
      window.console && window.console.log(e, e.keyCode)
      return
    }

    return false
  })

  // Widgets
  initWidgets()

  // Some special cases...
  $(document.body).on("click", "[data-hours-button]", function() {
    this.blur()
    const value = prompt(this.dataset.hoursButton)
    if (parseFloat(value)) {
      $("#id_modal-days")
        .val((parseFloat(value) / 8).toFixed(2))
        .focus()
    }
  })

  $(document.body).on("click", "[data-multiply-cost]", function() {
    const factor = parseFloat(this.dataset.multiplyCost),
      tpc = parseFloat($("#id_modal-third_party_costs").val()),
      cost = $("#id_modal-cost")

    if (tpc && factor) {
      cost.val((factor * tpc).toFixed(2)).focus()
    }
  })

  $(document.body).on("click", "[data-field-value]", function() {
    const field = $(this)
      .closest(".form-group")
      .find("input, textarea, select")
    field.val(this.dataset.fieldValue)
  })
})

function initWidgets() {
  function addZero(num) {
    return num < 10 ? "0" + num : "" + num
  }

  const invoicedOn = $("#id_invoiced_on")
  const dueOn = $("#id_due_on")
  if (invoicedOn.length && dueOn.length) {
    invoicedOn.on("change", function(_event) {
      const due = new Date(
        new Date(invoicedOn.val()).getTime() + 14 * 86400 * 1000
      )
      dueOn.val(
        addZero(due.getFullYear()) +
          "-" +
          addZero(1 + due.getMonth()) +
          "-" +
          addZero(due.getDate())
      )
    })
  }

  $("[data-autofill]:not(.initialized)").each(function() {
    const self = $(this),
      data = self.data("autofill"),
      sel = self.find("select")

    self.addClass("initialized")
    sel.on("change", function() {
      if (data["" + this.value]) {
        $.each(data["" + this.value], function(key, value) {
          self.find("[name$='" + key + "']").val(value)
        })
      }
    })
  })

  $("[data-autocomplete-id]:not(.initialized)").each(function() {
    const self = $(this),
      url = self.data("autocomplete-url"),
      id = self.data("autocomplete-id"),
      input = $("#" + id)

    self
      .addClass("initialized")
      .autocomplete({
        minLength: 2,
        source: function(request, response) {
          $.get(url, {q: request.term}, function(data) {
            response(data.results)
          })
        },
        focus: function(event, ui) {
          self.val(ui.item.label)
          return false
        },
        select: function(event, ui) {
          self.val(ui.item.label)
          input.val(ui.item.value).trigger("change")
          return false
        },
      })
      .on("focus", function() {
        this.select()
      })
  })

  $(document.body).on("click", "[data-clear]", function() {
    $(this.dataset.clear)
      .val("")
      .trigger("change")
  })

  $(document.body).on("click", "[data-convert]", function() {
    const params = new URLSearchParams()
    params.append("day", $("#id_modal-rendered_on").val())
    params.append("currency", $("#id_modal-expense_currency").val())
    params.append("cost", $("#id_modal-expense_cost").val())
    console.log(params)
    console.log(params.toString())

    $.getJSON("/expenses/convert/?" + params.toString(), function(data) {
      $("#id_modal-third_party_costs").val(data.cost)
    })
  })
}

window.addInlineForm = function addInlineForm(slug, onComplete) {
  const totalForms = $("#id_" + slug + "-TOTAL_FORMS"),
    newId = parseInt(totalForms.val())

  totalForms.val(newId + 1)
  const empty = $("#" + slug + "-empty"),
    attributes = ["id", "name", "for"],
    form = $(empty.html())

  form.removeClass("empty").attr("id", slug + "-" + newId)

  for (let i = 0; i < attributes.length; ++i) {
    const attr = attributes[i]

    form.find("*[" + attr + "*=__prefix__]").each(function() {
      const el = $(this)
      el.attr(attr, el.attr(attr).replace(/__prefix__/, newId))
    })
  }

  // insert the form after the last sibling with the same tagName
  // cannot use siblings() here, because the empty element may be the
  // only one (if no objects exist until now)
  form
    .insertAfter(empty.parent().children("[id|=" + slug + "]:last"))
    .hide()
    .fadeIn()

  if (onComplete) onComplete(form)

  return false
}
