from snapshottest import TestCase
from global_schema import schema


class APITestCase(TestCase):

    def test_product_class_all_fields(self):
        query = """
{
  productClassList (first: 5){
    edges {
      node {
        classId
        typeId
        className
        displayName
        isSystem
        productType {
          typeId
        }
      }
    }
  }
}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_pipelines_all_fields(self):
        query = """
{
  pipelinesList (first: 3){
    edges {
      node {
        pipelineId
        groupId
        displayName
        name
        orderNumber
        userId
        version
        versionDate
        description
        pipelineStageId
        xmlWorkflow
        pipelineStatusId
        multidataset
        readme
        anyOutputClass
        group {
          groupId
        }
        pipelineStage {
          pipelineStageId
        }
        pipelineStatus {
          pipelineStatusId
        }
        user {
          userId
        }
        processes {
          processId
        }
      }
    }
  }
}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_modules_all_fields(self):
        query = """
{
  modulesList (first: 3){
    edges {
      node {
        moduleId
        name
        version
        displayName
        xmlConfig
        description
        versionDate
        grade
        userId
        user {
          userId
        }
        pipelinesModules {
          edges {
            node {
              pipelineId
            }
          }
        }
      }
    }
  }
}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_group_pypelines_all_fields(self):
        query = """
{
	groupPypelinesList (first: 5) {
    edges {
      node {
        groupId
        name
        parentGroupId
        orderNumber
        displayName
        parentGroup {
          groupId
        }
      }
    }
  }
}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_pipelines_modules_all_fields(self):
        query = """
{
pipelinesModulesList (first: 3){
  edges {
    node {
      pipelineId
      moduleId
      xmlConfig
      module {
        moduleId
      }
      pipeline {
        pipelineId
      }
    }
  }
}
}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_pipeline_stage_all_fields(self):
        query = """
{
pipelineStageList {
  edges {
    node {
      pipelineStageId
      name
      displayName
      level
    }
  }
}
}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_product_type_all_fields(self):
        query = """
{
  productTypeList (first: 5){
    edges {
      node {
        typeId
        typeName
        displayName
      }
    }
  }
}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_mask_all_fields(self):
        query = """
{
maskList (first: 3){
  edges {
    node {
      maskId
      filter
      date
      flagRemoved
      tagId
      fieldId
      tableId
      table {
        tableId
      }
      tag {
        tagId
      }
      field {
        fieldId
      }
    }
  }
}
}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_map_all_fields(self):
        query = """
{
mapList (first: 3){
  edges {
    node {
      mapId
      tagId
      nside
      filter
      date
      flagRemoved
      ordering
      fieldId
      tableId
      image
      snr
      type
      magnitude
      table {
        tableId
      }
      tag {
        tagId
      }
    }
  }
}
}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_catalog_all_fields(self):
        # status - missing CatalogStatus
        query = """
{
catalogList (first: 3){
  edges {
    node {
      catalogId
      numTiles
      numObjects
      numColumns
      visibility
      catalogName
      version
      ingestionDate
      userId
      description
      statusId
      flagRemoved
      tableId
      table {
        tableId
      }
    }
  }
}
}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_filters_all_fields(self):
        query = """
{filtersList (first: 5){
  edges {
    node {
      id
      filter
      lambdaMin
      lambdaMax
      lambdaMean
    }
  }
}
}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_release_tag_all_fields(self):
        query = """
{releaseTagList (first: 3){
  edges {
    node {
      tagId
      name
      version
      releaseDate
      description
      docUrl
      releaseDisplayName
      fields {
        edges {
          node {
            fieldId
          }
        }
      }
    }
  }
}
}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_fields_all_fields(self):
        query = """
{fieldsList (first: 3){
  edges {
    node {
      fieldId
      fieldName
      displayName
      installDate
      releaseDate
      status
      startDate
      discoveryDate
      releaseTagId
      releaseTag {
        tagId
      }
    }
  }
}
}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_processes_all_fields(self):
        # PipelinesConfig - config
        # ProcessingSite - processing_site
        query = """
{processesList {
  edges {
    node {
      processId
      xmlConfig
      sessionId
      startTime
      endTime
      xmlBeforeRun
      namespace
      name
      processDir
      expirationTime
      idSite
      pypeInput
      comments
      startIngestion
      endIngestion
      flagPublished
      publishedDate
      readme
      instance
      flagRemoved
      statusId
      size
      configId
      session {
        sessionId
      }
      processStatus {
        processStatusId
      }
      fields {
        edges {
          node {
            fieldId
          }
        }
      }
      inputs {
        edges {
          node {
            productId
          }
        }
      }
      products {
        edges {
          node {
            productId
          }
        }
      }
      processComments {
        edges {
          node {
            processId
          }
        }
      }
      savedProcesses {
        processId
      }
    }
  }
}
}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_products_all_fields(self):
        query = """
{productsList (first: 3){
  edges {
    node {
      productId
      fileId
      jobId
      tableId
      classId
      processId
      flagRemoved
      displayName
      version
      selectedName
      Class {
        classId
      }
      file {
        fileId
      }
      job {
        jobId
      }
      table {
        tableId
      }
      process {
        processId
      }
    }
  }
}
}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    # Endpoints to review
    # def test_product_class_by_class_name(self):
    # def test_pipelines_by_name(self):
    # def test_modules_by_name(self):
    # def test_process_by_process_id(self):
    # def test_fields_by_tag_id(self):
    # def test_pipelines_by_field_id_and_stage_id(self):
    # def test_fields_by_tag_id(self):
    # def test_pipelines_by_field_id_and_stage_id(self):
    # def test_processes_by_field_id_and_pipeline_id(self):
    # def test_products_by_process_id(self):
    # def test_comments_by_process_id(self):
    # def test_fields_by_tagname(self):
    # def test_product_class_by_type_id(self):
    # def test__all_fields(self):

    def test_nested_sort(self):
        query = """
{
  productClassList(sort : [producttype_type_id_asc, productclass_display_name_asc], first : 5){
    edges {
      node {
        typeId
        displayName
        productType {
          typeId
          displayName
        }
      }
    }
  }
}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_search_same_table(self):
        query = """
{productClassList (search: {text: "sim", columns:product_class_class_name}, first: 3){
  edges {
    node {
      className
      displayName
    }
  }
}}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_search_nested_table(self):
        query = """
{productClassList (search: {text: "cata", columns:[product_type_type_name]}, first: 3){
  edges {
    node {
      className
      displayName
      productType {
        typeName
      }
    }
  }
}}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_search_and_sort(self):
        query = """
{productClassList (search: {text: "cata", columns:[product_type_type_name]}, sort: productclass_display_name_asc, first: 3){
  edges {
    node {
      className
      displayName
      productType {
        typeName
      }
    }
  }
}}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_pipelines(self):
        query = """
{pipelinesList(search: {text: "a", columns: [pipelines_name, pipelines_display_name, pipelines_version_date, tg_user_display_name, group_pypelines_display_name, pipeline_stage_name, pipelines_readme]}, first: 5, after: "YXJyYXljb25uZWN0aW9uOjA=") {
  edges {
    cursor
    node {
      name
      displayName
      versionDate
      user {
        displayName
      }
      group {
        displayName
      }
      pipelineStage {
        displayName
      }
      readme
    }
  }
}
}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_pipelines_modules(self):
        query = """
{pipelinesModulesList(first: 5, after: "YXJyYXljb25uZWN0aW9uOjI=") {
  edges {
    cursor
    node {
      pipeline {
        displayName
      }
      module {
        displayName
        name
        version
        versionDate
        user {
          displayName
        }
      }
    }
  }
}
}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_product_class(self):
        query = """
{productClassList (first: 5, after: "YXJyYXljb25uZWN0aW9uOjI="){
edges {
  cursor
  node {
    className
    displayName
    productType {
      displayName
      typeName
    }
  }
}
}
}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_fields(self):
        query = """
{fieldsList (sort: releasetag_tag_id_asc, search : {text : "Y1A1", columns: [fields_display_name, fields_field_name, release_tag_release_display_name, release_tag_name]}, first: 5){
  edges {
    node {
      fieldId
      fieldName
      releaseTag {
        tagId
        name
      }
    }
  }
}}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_processes(self):
        query = """
{processesList(first: 5, search: {text: "Ins", columns: [processes_name, process_status_display_name, fields_display_name, release_tag_release_display_name, tg_user_display_name]}) {
  pageInfo {
    startCursor
    endCursor
  }
  totalCount
  edges {
    cursor
    node {
      processId
      startTime
      endTime
      name
      flagPublished
      instance
      savedProcesses {
        savedDate
        savedDateEnd
      }
      processStatus{
        name
      }
      session {
          user{
          displayName
        }
      }
      fields {
        edges {
          node {
              fieldName
              releaseTag {
              releaseDisplayName
            }
          }
        }
      }
    }
  }
}
}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_products(self):
        query = """
{productsList (first: 5, search: {text: "1073", columns: [products_process_id]}, sort:products_display_name_asc){
  edges {
    node {
      productId
      displayName
      process {
        processId
      }
    }
  }
}}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_release_tag_only_available_true(self):
        query = """
{releaseTagList (search: {text: "Y1", columns: [release_tag_release_display_name, release_tag_name, fields_display_name, fields_field_name]}, onlyAvailable :true, first: 5){
  edges {
    node {
      releaseDisplayName
      name
      version
      releaseDate
      description
      docUrl
      tagId
      fields {
        edges {
          node {
            status
          }
        }
      }
    }
  }
}
}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_release_tag(self):
        query = """
{releaseTagList (search: {text: "Y1", columns: [release_tag_release_display_name, release_tag_name]}, first: 5){
  edges {
    node {
      releaseDisplayName
      name
      version
      releaseDate
      description
      docUrl
      tagId
      fields {
        edges {
          node {
            status
          }
        }
      }
    }
  }
}
}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_modules_pipelines(self):
        query = """
        {modulesList (first: 5, search: {text: "a", columns: [modules_display_name, modules_name, modules_version, modules_version_date, pipelines_display_name, tg_user_display_name]}){
          edges {
            node {
              moduleId
              name
              displayName
              user {
                userName
                displayName
              }
              pipelinesModules {
                edges {
                  node {
                    pipeline {
                      pipelineId
                      displayName
                      name
                    }
                  }
                }
              }
            }
          }
        }}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_pipelines_no_args(self):
        query = """
{pipelinesByStageIdAndTagIdAndFieldId (first: 3){
  edges {
    node {
      pipelineId
      pipelineName
      pipelineDisplayName
      stageDisplayName
      processCount
      lastProcessId
      lastProcessStartTime
      lastProcessEndTime
      lastProcessStatus
    }
  }
}
}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_pipelines_by_stage_id_and_tag_id_and_field_id(self):
        query = """
{pipelinesByStageIdAndTagIdAndFieldId (first: 3, stageId: 9, fieldId: 40, tagId: 24){
  edges {
    node {
      pipelineId
      pipelineName
      pipelineDisplayName
      stageDisplayName
      processCount
      lastProcessId
      lastProcessStartTime
      lastProcessEndTime
      lastProcessStatus
    }
  }
}
}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_time_profile(self):
        query = """
{timeProfile(processId: 10031073, first: 2){
  edges{
    node{
      displayName
      moduleName
			jobs {
        hid
        startTime
        endTime
      }
    }
  }
}
}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_processes_by_tag_id_and_field_id_and_pipeline_id(self):
        query = """
{processesByTagIdAndFieldIdAndPipelineId (pipelineId: 214, fieldId: 40, tagId: 24){
	processId
  startTime
  endTime
  name
}
}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_output_products_by_pipeline(self):
        query = """
{outputProductsByPipeline(pipelineId:200){
  edges{
    node {
      displayName
      products
    }
  }
}
}
        """
        self.assertMatchSnapshot(schema.execute(query).data)

    def test_input_products_by_pipeline(self):
        query = """
{inputProductsByPipeline(pipelineId:176) {
  edges {
    node {
      displayName
      moduleName
      products
    }
  }
}
}
        """
        self.assertMatchSnapshot(schema.execute(query).data)
