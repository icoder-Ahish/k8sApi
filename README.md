# Kubernetes Api Call

# Import Required Module

    import streamlit as st
    from kubernetes import client, config

# Load the Kubernetes configuration
    config.load_kube_config()

# Create a Kubernetes API client for the Deployment API
    Appsapi = client.AppsV1Api()
    CoreApi = client.CoreV1Api()


# Get all the namespaces in the cluster
    namespaces = CoreApi.list_namespace()

# Create a list of namespace names
    namespace_names = [ns.metadata.name for ns in namespaces.items]

# Add a selectbox to the Streamlit app with all the namespace names
    selected_namespace = st.sidebar.selectbox("Select Namespace", namespace_names)

# Print the selected namespace
    st.write("You selected namespace:", selected_namespace)

# List all deployments in the selected namespace
    deployments = Appsapi.list_namespaced_deployment(selected_namespace).items

# Display the name and the number of replicas for each deployment
    for deployment in deployments:
        st.write("Deployment Name:", deployment.metadata.name)
        st.write("Replicas:", deployment.spec.replicas)
        st.write("----")
# Run this application
    streamlit run filename.py
