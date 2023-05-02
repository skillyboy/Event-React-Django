import React, { useState } from "react";
import axios from "axios";

function EventCreatePage() {
  const [eventData, setEventData] = useState({
    event_name: "",
    date: "",
    time: "",
    location: "",
    image: null,
  });

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setEventData((prevEventData) => ({
      ...prevEventData,
      [name]: value,
    }));
  };

  const handleImageChange = (event) => {
    setEventData((prevEventData) => ({
      ...prevEventData,
      image: event.target.files[0],
    }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    axios
      .post("/event/create", eventData, {
        headers: {
          "X-CSRFToken": getCookie("csrftoken"),
        },
      })
      .then((response) => {
        console.log(response.data);
        // TODO: handle success
      })
      .catch((error) => {
        console.log(error.response.data);
        // TODO: handle error
      });
  };

  // Utility function to get the CSRF token from cookies
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="event_name">Event name:</label>
        <input
          type="text"
          id="event_name"
          name="event_name"
          value={eventData.event_name}
          onChange={handleInputChange}
        />
      </div>
      <div>
        <label htmlFor="date">Date:</label>
        <input
          type="date"
          id="date"
          name="date"
          value={eventData.date}
          onChange={handleInputChange}
        />
      </div>
      <div>
        <label htmlFor="time">Time:</label>
        <input
          type="time"
          id="time"
          name="time"
          value={eventData.time}
          onChange={handleInputChange}
        />
      </div>
      <div>
        <label htmlFor="location">Location:</label>
        <input
          type="text"
          id="location"
          name="location"
          value={eventData.location}
          onChange={handleInputChange}
        />
      </div>
      <div>
        <label htmlFor="image">Image:</label>
        <input
          type="file"
          id="image"
          name="image"
          accept="image/*"
          onChange={handleImageChange}
        />
      </div>
      <button type="submit">Create event</button>
    </form>
  );
}

export default EventCreatePage;
