import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHeart } from '@fortawesome/free-solid-svg-icons';

const EventListView = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    const fetchEvents = async () => {
      try {
        const response = await axios.get('/eventslist/');
        setEvents(response.data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchEvents();
  }, []);

  const handleLikeEvent = async (eventId, isLiked) => {
    try {
      const response = await axios.post(`/event/${eventId}/like/`, { is_liked: !isLiked });
      const updatedEvents = events.map((event) => {
        if (event.id === response.data.id) {
          return { ...event, likes_count: response.data.likes_count, is_liked: response.data.is_liked };
        } else {
          return event;
        }
      });
      setEvents(updatedEvents);
    } catch (error) {
      console.error(error);
    }
  };

  const renderEvents = () => {
    return events.map((event) => (
      <div key={event.id} className="event-card">
        <h3>{event.event_name}</h3>
        <p>Date: {event.date}</p>
        <p>Time: {event.time}</p>
        <p>Location: {event.location}</p>
        <div className="like-container">
          <FontAwesomeIcon icon={faHeart} onClick={() => handleLikeEvent(event.id, event.is_liked)} className={`like-icon ${event.is_liked ? 'liked' : ''}`} />
          <span className="likes">{event.likes_count} Likes</span>
        </div>
        <img src={event.image} alt={event.event_name} />
      </div>
    ));
  };

  return (
    <div className="event-list-view">
      <h1>All Upcoming Events</h1>
      {renderEvents()}
    </div>
  );
};

export default EventListView;
