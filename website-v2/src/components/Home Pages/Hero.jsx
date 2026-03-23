import React from 'react';
import mainImage from '../IMAGES/Home Page images/main.png';
import SEO from "../SEO";
import { seoConfig } from '../../lib/seo.config';

const Hero = () => {
    return (
    <>
        <SEO
            title="Best AI Consulting and Development Company - AiGENThix"
            description="AiGENThix is a leading AI consulting and development company building cutting-edge Generative AI, Machine Learning, Robotics, and enterprise AI solutions for startups and enterprises."
            keywords="AI consulting company, AI development, generative AI solutions, machine learning services, ethical AI, enterprise AI, AiGENThix"
            structuredData={[seoConfig.organization, seoConfig.website]}
            url="/"
            image="/hero-og.jpg"
        />

        {/* HERO */}
        <div 
            className="bg-[#0B2847] text-white flex items-center justify-center relative overflow-hidden
                       pt-[80px] pb-12 
                       min-h-[calc(100vh-70px)] lg:h-[calc(100vh-70px)]"
        >
            <div className="max-w-7xl mx-auto px-6 sm:px-10 lg:px-16 w-full">
                
                <div className="flex flex-col-reverse lg:flex-row items-center justify-between gap-10 lg:gap-12">

                    {/* LEFT */}
                    <div className="w-full lg:w-[45%] text-center lg:text-left">
                        
                        <h1 
                            className="text-2xl sm:text-3xl md:text-4xl lg:text-5xl leading-tight mb-4 sm:mb-5 font-serif"
                            style={{ fontFamily: 'Georgia, "Times New Roman", serif', fontWeight: '400' }}
                        >
                            Envisioning the Future with Ethical AI
                        </h1>

                        <p className="text-base sm:text-lg lg:text-xl font-normal mb-6 sm:mb-8 lg:mb-10 leading-relaxed max-w-xl mx-auto lg:mx-0 opacity-95">
                            We build cutting-edge AI solutions for startups and enterprises
                        </p>

                        <a
                            href="/contact"
                            className="inline-block bg-[#2D4DE8] hover:bg-[#1a39d1] text-white font-medium py-3 px-7 sm:px-8 text-sm sm:text-base transition duration-300 shadow-lg hover:shadow-xl"
                        >
                            Get in touch
                        </a>
                    </div>

                    {/* RIGHT IMAGE */}
                    <div className="w-full lg:w-[50%] flex justify-center lg:justify-end">
                        <div className="w-full max-w-[420px] sm:max-w-[480px] lg:max-w-[520px]">
                            
                            <div className="h-[220px] sm:h-[280px] md:h-[320px] lg:h-[400px] flex items-center justify-center">
                                <img 
                                    src={mainImage} 
                                    alt="AI Development Platform"
                                    className="w-full h-full object-contain drop-shadow-2xl transition-transform duration-700 hover:scale-105"
                                />
                            </div>

                        </div>
                    </div>

                </div>
            </div>
        </div>
    </>
    );
};

export default Hero;