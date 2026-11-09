
const API_KEY = process.env.NEXT_PUBLIC_WEATHER_API_KEY;
const BASE_URL = "https://api.openweathermap.org/data/2.5";

if (!API_KEY) {
  console.error("No se encontró NEXT_PUBLIC_WEATHER_API_KEY");
}

export async function getWeatherByCity(city) {
  if (!API_KEY) {
    throw new Error("Falta configurar la API Key de OpenWeatherMap.");
  }

  const res = await fetch(
    `${BASE_URL}/weather?q=${encodeURIComponent(city)}&units=metric&lang=es&appid=${API_KEY}`
  );

  if (!res.ok) {
    throw new Error("No se encontró la ciudad solicitada.");
  }

  return res.json();
}

export async function getWeatherByCoords(lat, lon) {
  if (!API_KEY) {
    throw new Error("Falta configurar la API Key de OpenWeatherMap.");
  }

  const res = await fetch(
    `${BASE_URL}/weather?lat=${lat}&lon=${lon}&units=metric&lang=es&appid=${API_KEY}`
  );

  if (!res.ok) {
    throw new Error("Error al consultar el clima para tu ubicación.");
  }

  return res.json();
}
