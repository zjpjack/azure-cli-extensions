# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VirtualMachine(Model):
    """Define the virtualMachine.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param resource_pool_id: Gets or sets the ARM Id of the resourcePool
     resource on which this virtual machine will
     deploy.
    :type resource_pool_id: str
    :param template_id: Gets or sets the ARM Id of the template resource to
     deploy the virtual machine.
    :type template_id: str
    :param v_center_id: Gets or sets the ARM Id of the vCenter resource in
     which this resource pool resides.
    :type v_center_id: str
    :param os_profile: OS properties.
    :type os_profile: ~azure.mgmt.vmware.v2020_10_01_preview.models.OsProfile
    :param hardware_profile: Hardware properties.
    :type hardware_profile:
     ~azure.mgmt.vmware.v2020_10_01_preview.models.HardwareProfile
    :param network_profile: Network properties.
    :type network_profile:
     ~azure.mgmt.vmware.v2020_10_01_preview.models.NetworkProfile
    :param storage_profile: Storage properties.
    :type storage_profile:
     ~azure.mgmt.vmware.v2020_10_01_preview.models.StorageProfile
    :param mo_ref_id: Gets or sets the vCenter MoRef (Managed Object
     Reference) ID for the virtual machine.
    :type mo_ref_id: str
    :param inventory_item_id: Gets or sets the inventory Item ID for the
     virtual machine.
    :type inventory_item_id: str
    :ivar mo_name: Gets or sets the vCenter Managed Object name for the
     virtual machine.
    :vartype mo_name: str
    :ivar folder_path: Gets or sets the folder path of the vm.
    :vartype folder_path: str
    :ivar instance_uuid: Gets or sets the instance uuid of the vm.
    :vartype instance_uuid: str
    :ivar power_state: Gets the power state of the virtual machine.
    :vartype power_state: str
    :ivar custom_resource_name: Gets the name of the corresponding resource in
     Kubernetes.
    :vartype custom_resource_name: str
    :ivar uuid: Gets or sets a unique identifier for this resource.
    :vartype uuid: str
    :ivar provisioning_state: Gets or sets the provisioning state.
    :vartype provisioning_state: str
    :param location: Required. Gets or sets the location.
    :type location: str
    :param extended_location: Gets or sets the extended location.
    :type extended_location:
     ~azure.mgmt.vmware.v2020_10_01_preview.models.ExtendedLocation
    :param system_data: The system data.
    :type system_data:
     ~azure.mgmt.vmware.v2020_10_01_preview.models.SystemData
    :param tags: Gets or sets the Resource tags.
    :type tags: dict[str, str]
    :ivar name: Gets or sets the name.
    :vartype name: str
    :ivar id: Gets or sets the Id.
    :vartype id: str
    :ivar type: Gets or sets the type of the resource.
    :vartype type: str
    :param kind: Metadata used by portal/tooling/etc to render different UX
     experiences for resources of the same type; e.g. ApiApps are a kind of
     Microsoft.Web/sites type.  If supported, the resource provider must
     validate and persist this value.
    :type kind: str
    """

    _validation = {
        'mo_name': {'readonly': True},
        'folder_path': {'readonly': True},
        'instance_uuid': {'readonly': True},
        'power_state': {'readonly': True},
        'custom_resource_name': {'readonly': True},
        'uuid': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'location': {'required': True},
        'name': {'readonly': True},
        'id': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'resource_pool_id': {'key': 'properties.resourcePoolId', 'type': 'str'},
        'template_id': {'key': 'properties.templateId', 'type': 'str'},
        'v_center_id': {'key': 'properties.vCenterId', 'type': 'str'},
        'os_profile': {'key': 'properties.osProfile', 'type': 'OsProfile'},
        'hardware_profile': {'key': 'properties.hardwareProfile', 'type': 'HardwareProfile'},
        'network_profile': {'key': 'properties.networkProfile', 'type': 'NetworkProfile'},
        'storage_profile': {'key': 'properties.storageProfile', 'type': 'StorageProfile'},
        'mo_ref_id': {'key': 'properties.moRefId', 'type': 'str'},
        'inventory_item_id': {'key': 'properties.inventoryItemId', 'type': 'str'},
        'mo_name': {'key': 'properties.moName', 'type': 'str'},
        'folder_path': {'key': 'properties.folderPath', 'type': 'str'},
        'instance_uuid': {'key': 'properties.instanceUuid', 'type': 'str'},
        'power_state': {'key': 'properties.powerState', 'type': 'str'},
        'custom_resource_name': {'key': 'properties.customResourceName', 'type': 'str'},
        'uuid': {'key': 'properties.uuid', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'extended_location': {'key': 'extendedLocation', 'type': 'ExtendedLocation'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
    }

    def __init__(self, *, location: str, resource_pool_id: str=None, template_id: str=None, v_center_id: str=None, os_profile=None, hardware_profile=None, network_profile=None, storage_profile=None, mo_ref_id: str=None, inventory_item_id: str=None, extended_location=None, system_data=None, tags=None, kind: str=None, **kwargs) -> None:
        super(VirtualMachine, self).__init__(**kwargs)
        self.resource_pool_id = resource_pool_id
        self.template_id = template_id
        self.v_center_id = v_center_id
        self.os_profile = os_profile
        self.hardware_profile = hardware_profile
        self.network_profile = network_profile
        self.storage_profile = storage_profile
        self.mo_ref_id = mo_ref_id
        self.inventory_item_id = inventory_item_id
        self.mo_name = None
        self.folder_path = None
        self.instance_uuid = None
        self.power_state = None
        self.custom_resource_name = None
        self.uuid = None
        self.provisioning_state = None
        self.location = location
        self.extended_location = extended_location
        self.system_data = system_data
        self.tags = tags
        self.name = None
        self.id = None
        self.type = None
        self.kind = kind