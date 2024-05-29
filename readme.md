# Alt Text Generator API 

This is a fast API project that generates image alt text using the Gpt4 Vision API or the Replicate AI API. It provides an easy way to automatically generate descriptive text for images, improving accessibility and SEO.

## Features

- Generate alt text for images using Gpt4 Vision API or Replicate AI API.
- Free hosted solution available at [https://alt-text-generator.vercel.app](https://alt-text-generator.vercel.app).

## Gpt4 Vision API

Gpt4 Vision is a powerful AI model that can analyze images and generate descriptive alt text. To use the Gpt4 Vision API, you will need an API key. You can obtain an API key by signing up on the Gpt4 Vision website.

## Replicate AI API

Replicate AI is another AI model that specializes in image analysis and alt text generation. To use the Replicate AI API, you will need an API key. You can obtain an API key by signing up on the Replicate AI website.

## Setup

To set up the project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/alt-text-generator.git`
2. Install the dependencies: `pip install -r requirements.txt`
3. Set up your API key in the configuration file.
4. Run the application: `python main.py`

## Deploying to Vercel

To deploy the project to Vercel, follow these steps:

1. Sign up for a Vercel account at [https://vercel.com](https://vercel.com).
2. Install the Vercel CLI: `npm install -g vercel`.
3. Navigate to the project directory: `cd alt-text-generator`.
4. Run the deployment command: `vercel`.
5. Follow the prompts to configure your deployment settings.
6. Once the deployment is complete, your project will be live at the provided URL.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Hosting on AWS Lambda

If you prefer to host the project on AWS Lambda, follow these steps:

1. Create an AWS Lambda function.
2. Set up the necessary environment variables, including your API key.
3. Upload the project code to the Lambda function.
4. Configure the API Gateway to trigger the Lambda function.
5. Test the API endpoint to ensure everything is working correctly.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).