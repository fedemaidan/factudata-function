local-build:
	docker build -t flask-image:v1 .

local-run:
	docker run -p 5000:8080 --env-file ./dev.env flask-image:v1

local-build-run:
	make local-build
	make local-run

prod-deploy:
	gcloud config set run/region us-central1
	gcloud run deploy

prod-test:
	curl -X POST -H "Content-Type: application/json" -d '{"filename": "https://firebasestorage.googleapis.com/v0/b/factudata-3afdf.appspot.com/o/probandoFiles%2FBEST%20PHONE%2001-03.jpeg?alt=media&token=caf9169b-419e-431b-bc49-0aa74afe8520&_gl=1*g1ar7g*_ga*MTY0ODY5NjU1MS4xNjg1MDQzNTU1*_ga_CW55HF8NVT*MTY4NjY4Mzc2MS4yMi4xLjE2ODY2ODU3NjAuMC4wLjA.", "id": "jWtXVShdwsQk96irTh4K"}' https://factudata-function-4tbluuq42q-uc.a.run.app