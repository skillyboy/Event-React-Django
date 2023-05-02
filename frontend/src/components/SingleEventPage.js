import React from "react";
import { useParams } from "react-router-dom";

function SingleEventPage() {
  const { eventId } = useParams();

  // Use the eventId to fetch the event details from the server and render them

  return (
    <div>
      <h1>Event Details</h1>
      <p>Event ID: {eventId}</p>
      {/* Render the rest of the event details */}
    </div>
  );
}

export default SingleEventPage;
