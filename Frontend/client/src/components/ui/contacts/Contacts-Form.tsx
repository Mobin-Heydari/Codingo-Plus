"use client";

import React from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import ContactsServer from '@/components/server/contacts/Contact-API';

// Define the FormData interface with full_name
interface FormData {
    full_name: string;
    email: string;
    message: string;
    phone: string;
}

const ContactsForm: React.FC = () => {
    const initialValues: FormData = {
        full_name: '', // Initialize full_name
        email: '',
        message: '',
        phone: '' // Initialize phone
    };

    const validationSchema = Yup.object({
        full_name: Yup.string().required('Name is required'), // Update to match the new property
        email: Yup.string()
            .email('Invalid email format')
            .required('Email is required'),
        message: Yup.string().required('Message is required'),
        phone: Yup.string()
            .length(11, 'Phone number must be exactly 11 digits')
            .matches(/^\d+$/, 'Phone number must be digits only')
            .required('Phone number is required')
    });

    const handleSubmit = async (values: FormData, { setSubmitting, resetForm }: any) => {
        try {
            await ContactsServer.postContact(values); // Call the post function
            resetForm(); // Reset the form after successful submission
        } catch (error) {
            console.error('Error posting contact data:', error);
        } finally {
            setSubmitting(false); // Set submitting to false after submission
        }
    };

    return (
        <Formik
            initialValues={initialValues}
            validationSchema={validationSchema}
            onSubmit={handleSubmit}
        >
            {({ isSubmitting }) => (
                <Form>
                    <div>
                        <Field type="text" name="full_name" placeholder="Your Name" />
                        <ErrorMessage name="full_name" component="div" />
                    </div>
                    <div>
                        <Field type="email" name="email" placeholder="Your Email" />
                        <ErrorMessage name="email" component="div" />
                    </div>
                    <div>
                        <Field as="textarea" name="message" placeholder="Your Message" />
                        <ErrorMessage name="message" component="div" />
                    </div>
                    <div>
                        <Field type="text" name="phone" placeholder="Your Phone Number" />
                        <ErrorMessage name="phone" component="div" />
                    </div>
                    <button type="submit" disabled={isSubmitting}>
                        Submit
                    </button>
                </Form>
            )}
        </Formik>
    );
};

export default ContactsForm;