const fetchUserData = async (id) => {
  try {
    const res = await fetch(`https://api.example.com/users/${id}`);
    if (!res.ok) throw new Error("Request failed");
    const data = await res.json();
    return data;
  } catch (err) {
    console.error("Error fetching user:", err);
  }
};

fetchUserData(1).then((user) => console.log(user));
