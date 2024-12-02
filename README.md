### **Summary Table of Endpoints**


| **Endpoint** | **Request Method** | **Description** | **Parameters** | **Sample JSON Payload** |
| --- | --- | --- | --- | --- |
| `/users/` | POST | Create a new user | `username`, `email`, `password`, `first_name`, `last_name`, `phone_number`, `user_role` | `{ "username": "johndoe", "email": "`[`johndoe@example.com`](mailto:johndoe@example.com)`", "password": "securePass123", "first_name": "John", "last_name": "Doe", "phone_number": "123456789", "user_role": "USER" }` |
| `/users/` | GET | Get all users | None | None |
| `/users/<user_uuid>` | GET | Get user by UUID | `user_uuid` | None |
| `/users/<user_uuid>` | PUT | Update user by UUID | `user_uuid`, `username`, `email`, `first_name`, `last_name`, `phone_number`, `user_role` | `{ "username": "updatedUser", "email": "`[`updated@example.com`](mailto:updated@example.com)`", "first_name": "Updated", "last_name": "User", "phone_number": "987654321", "user_role": "ADMIN" }` |
| `/users/<user_uuid>` | DELETE | Delete user by UUID | `user_uuid` | None |
| `/tours/` | POST | Create a new tour | `tour_name`, `description`, `price`, `start_date`, `end_date`, `seats_available`, `image_url` | `{ "tour_name": "Beach Adventure", "description": "Enjoy a wonderful beach experience", "price": 500.00, "start_date": "2023-12-15", "end_date": "2023-12-20", "seats_available": 30, "image_url": "`[`http://example.com/image.jpg`](http://example.com/image.jpg)`" }` |
| `/tours/` | GET | Get all tours | None | None |
| `/tours/<tour_uuid>` | GET | Get tour by UUID | `tour_uuid` | None |
| `/tours/<tour_uuid>` | PUT | Update tour by UUID | `tour_uuid`, `tour_name`, `description`, `price`, `start_date`, `end_date`, `seats_available`, `image_url` | `{ "tour_name": "Updated Tour", "description": "Updated description", "price": 600.00, "start_date": "2023-12-10", "end_date": "2023-12-15", "seats_available": 25, "image_url": "`[`http://example.com/updated_image.jpg`](http://example.com/updated_image.jpg)`" }` |
| `/tours/<tour_uuid>` | DELETE | Delete tour by UUID | `tour_uuid` | None |
| `/bookings/` | POST | Create a new booking | `user_uuid`, `tour_uuid`, `travel_date`, `seats_booked` | `{ "user_uuid": "123e4567-e89b-12d3-a456-426614174000", "tour_uuid": "223e4567-e89b-12d3-a456-426614174001", "travel_date": "2023-12-15", "seats_booked": 2 }` |
| `/bookings/` | GET | Get all bookings | None | None |
| `/bookings/<booking_uuid>` | GET | Get booking by UUID | `booking_uuid` | None |
| `/bookings/<booking_uuid>` | DELETE | Delete booking by UUID | `booking_uuid` | None |
| `/payments/` | POST | Create a payment | `booking_uuid`, `user_uuid`, `amount`, `payment_method` | `{ "booking_uuid": "333e4567-e89b-12d3-a456-426614174002", "user_uuid": "123e4567-e89b-12d3-a456-426614174000", "amount": 1000.00, "payment_method": "GCASH" }` |
| `/payments/` | GET | Get all payments | None | None |
| `/payments/<payment_uuid>` | GET | Get payment by UUID | `payment_uuid` | None |
| `/reviews/` | POST | Create a review | `tour_uuid`, `user_uuid`, `rating`, `comment` | `{ "tour_uuid": "223e4567-e89b-12d3-a456-426614174001", "user_uuid": "123e4567-e89b-12d3-a456-426614174000", "rating": 5, "comment": "Amazing tour experience!" }` |
| `/reviews/<tour_uuid>` | GET | Get reviews for a tour | `tour_uuid` | None |
