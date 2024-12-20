"use client";

import React, { useRef, useEffect } from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import ContactsServer from '@/components/server/contacts/Contact-API';

interface FormData {
    full_name: string;
    email: string;
    message: string;
    phone: string;
}

const ContactsForm: React.FC = () => {
    const initialValues: FormData = {
        full_name: '',
        email: '',
        message: '',
        phone: ''
    };

    const validationSchema = Yup.object({
        full_name: Yup.string().required('لطفا نام خود را وارد کنید'),
        email: Yup.string()
            .email('فرمت ایمیل صحیح نیست')
            .required('لطفا ایمیل خود را وارد کنید'),
        message: Yup.string().required('پیام خود را با در اشتراک بگذارید'),
        phone: Yup.string()
            .length(11, 'شماره تلفن خود را 11 رقمی وارد کنید')
            .matches(/^\d+$/, 'فقط اعداد را وارد کنید')
            .required('شماره تلفن خود را وارد کنید')
    });

    const handleSubmit = async (values: FormData, { setSubmitting, resetForm }: any) => {
        try {
            await ContactsServer.postContact(values);
            resetForm();
        } catch (error) {
            console.error('Error posting contact data:', error);
        } finally {
            setSubmitting(false);
        }
    };

    const TextareaAutoResize = ({ field, form }: any) => {
        const textareaRef = useRef<HTMLTextAreaElement>(null);

        const adjustHeight = () => {
            if (textareaRef.current) {
                textareaRef.current.style.height = 'auto'; // Reset height
                textareaRef.current.style.height = `${textareaRef.current.scrollHeight}px`; // Set to scroll height
            }
        };

        useEffect(() => {
            adjustHeight(); // Adjust height on mount
        }, []);

        return (
            <textarea
                {...field}
                ref={textareaRef}
                onInput={adjustHeight}
                placeholder="پیام محترم شما"
                className="p-3 border border-primary rounded-2xl resize-none overflow-hidden"
                style={{ minHeight: '50px', maxHeight: '300px' }} // Set min and max height
            />
        );
    };

    return (
        <Formik
            initialValues={initialValues}
            validationSchema={validationSchema}
            onSubmit={handleSubmit}
        >
            {({ isSubmitting }) => (
                <Form className="flex flex-col items-center p-5">
                    <div className="grid grid-cols-1 gap-4 w-full max-w-lg max-md:w-full">
                        <div className="flex flex-col gap-2">
                            <Field
                                type="text"
                                name="full_name"
                                placeholder="نام شما"
                                className="p-3 border border-secondary rounded-xl h-12"
                            />
                            <ErrorMessage name="full_name" component="div" className="text-red-500 text-sm" />
                        </div>
                        <div className="flex flex-col gap-2">
                            <Field
                                type="email"
                                name="email"
                                placeholder="ایمیل شما"
                                className="p-3 border border-secondary rounded-xl h-12"
                            />
                            <ErrorMessage name="email" component="div" className="text-red-500 text-sm" />
                        </div>
                        <div className="flex flex-col gap-2">
                            <Field
                                type="text"
                                name="phone"
                                placeholder="شماره تماس شما"
                                className="p-3 border border-secondary rounded-xl h-12 w-full"
                                style={{ width: '100%' }} // Full width
                            />
                            <ErrorMessage name="phone" component="div" className="text-red-500 text-sm" />
                        </div>
                    </div>
                    <div className="flex flex-col gap-2 w-full max-w-lg mt-4">
                        <Field name="message" component={TextareaAutoResize}/>
                        <ErrorMessage name="message" component="div" className="text-red-500 text-sm" />
                    </div>
                    <div className="flex justify-center w-full mt-4">
                        <button
                            type="submit"
                            disabled={isSubmitting}
                            className={`w-full md:w-1/4 p-2 text-white rounded-md ${isSubmitting ? 'bg-gray-400' : 'bg-secondary hover:bg-primary'} focus:outline-none`}
                        >
                            ارسال
                        </button>
                    </div>
                </Form>
            )}
        </Formik>
    );
};

export default ContactsForm;