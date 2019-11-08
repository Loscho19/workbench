import {containsJSON, createIdentifier} from "./utils.js"

const ACTIVE_PROJECTS = () => "/projects/projects/"
const PROJECT_SEARCH = q => `/projects/autocomplete/?only_open=1&q=${q}`
const SERVICES = id => `projects/${id}/services/`
const CREATE_HOURS = id => `projects/${id}/createhours/`
const endpoint = (fn, ...args) => fn(...args)

export function createActivity(dispatch, fields = {}) {
  dispatch({
    type: "ADD_ACTIVITY",
    activity: {
      description: "",
      seconds: 0,
      id: createIdentifier(),
      left: Math.floor(Math.random() * (window.innerWidth - 300)),
      top: Math.floor(Math.random() * (window.innerHeight - 300)),
      ...fields,
    },
  })
}

export async function fetchProjects(q) {
  const response = await fetch(endpoint(PROJECT_SEARCH, q), {
    credentials: "include",
  })
  if (containsJSON(response)) {
    const data = await response.json()
    return data.results
  }
  return []
}

export async function fetchServices(project) {
  const response = await fetch(endpoint(SERVICES, project), {
    credentials: "include",
  })
  if (containsJSON(response)) {
    const data = await response.json()
    return data.services.map(row => ({label: row[1], value: row[0]}))
  }
  return []
}

export async function loadProjects(dispatch) {
  const response = await fetch(endpoint(ACTIVE_PROJECTS), {
    credentials: "include",
  })
  if (containsJSON(response)) {
    const data = await response.json()
    dispatch({
      type: "PROJECTS",
      projects: data.projects,
    })
  }
}

export async function sendLogbook(dispatch, {activity, current, seconds}) {
  const url = endpoint(CREATE_HOURS, activity.project.value)

  if (
    !activity.description ||
    !activity.description.length ||
    !activity.service ||
    !seconds
  ) {
    const params = new URLSearchParams()
    if (activity.service) params.append("service", activity.service.value)
    params.append("description", activity.description)
    params.append("hours", Math.ceil(seconds / 360) / 10)

    dispatch({type: "STOP", current})
    dispatch({type: "MODAL_ACTIVITY", id: activity.id})
    const finalUrl = `${url}?${params.toString()}`
    console.log(finalUrl)
    window.openModalFromUrl(finalUrl)
    return
  }

  const body = new FormData()
  if (activity.service) body.append("service", activity.service.value)
  body.append("description", activity.description)
  body.append("hours", Math.ceil(seconds / 360) / 10)
  body.append(
    "rendered_by",
    document.getElementById("root").dataset.currentUser
  )
  body.append("rendered_on", new Date().toISOString().replace(/T.*/, ""))

  const headers = new Headers()
  headers.append("X-Requested-With", "XMLHttpRequest")
  headers.append("X-CSRFToken", document.cookie.match(/\bcsrftoken=(.+?)\b/)[1])

  const response = await fetch(url, {
    credentials: "include",
    method: "POST",
    body,
    headers,
  })
  if (response.status == 200) {
    window.initModal(await response.text())
  } else {
    dispatch({type: "STOP", current})
    dispatch({type: "UPDATE_ACTIVITY", id: activity.id, fields: {seconds: 0}})
    window.location.reload()
  }
}
