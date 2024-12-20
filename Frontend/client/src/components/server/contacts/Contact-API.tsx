interface ContactData {
    full_name: string;
    email: string;
    message: string;
    phone: string;
}
const ContactsServer = {
    postContact: async (data: ContactData): Promise<any> => {
        const response = await fetch('http://127.0.0.1:8000/contacts/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        return response.json(); // Return the response data if needed
    }
};

export default ContactsServer;