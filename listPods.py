import streamlit as st
from kubernetes import client, config

# Load kubeconfig file
config.load_kube_config()

# Create an instance of the API
api = client.CoreV1Api()

# Get all the namespaces in the cluster
namespaces = api.list_namespace()

# Create a list of namespace names
namespace_names = [ns.metadata.name for ns in namespaces.items]

# Add a selectbox to the Streamlit app with all the namespace names
selected_namespace = st.sidebar.selectbox("Select Namespace", namespace_names)

# Print the selected namespace
st.write("You selected namespace:", selected_namespace)
