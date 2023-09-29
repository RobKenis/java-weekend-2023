helm-add-falco:
	helm repo add falcosecurity https://falcosecurity.github.io/charts

.PHONY: helm
helm: helm-add-falco
	helm repo update

.PHONY: falco
falco:
	helm upgrade falco falcosecurity/falco --namespace falco --create-namespace -f falco.values.yaml --install