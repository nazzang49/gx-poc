import great_expectations as gx

# -- read default context from great_expectations.yml
context = gx.get_context()
# print(context)

# TODO check expectation suite loaded from GCS
# suite = context.get_expectation_suite("my_suite")
# print(suite)

# datasource = context.sources.add_or_update_sql(
#     name="my_bigquery_datasource",
#     connection_string="bigquery://my-proj-414213/tmp",
# )

# TODO 1. table asset
# table_asset = datasource.add_table_asset(name="my_table_table_asset", table_name="my_table")

# TODO 2. query asset
# query_asset = datasource.add_query_asset(name="my_table_query_asset", query="select * from my_table limit 1")

# -- create batch from asset
# request = table_asset.build_batch_request()

# -- create expectation suite and validator
# context.add_or_update_expectation_suite(expectation_suite_name="my_suite")
# validator = context.get_validator(
#     batch_request=request, expectation_suite_name="my_suite"
# )

# -- add expectations into expectation suite
# validator.expect_column_values_to_not_be_null(column="id")
# validator.expect_column_values_to_be_between(
#     column="age", min_value=35, max_value=40
# )

# -- save or update expectation suite to GCS
# validator.save_expectation_suite(discard_failed_expectations=False)

# -- checkpoint including
# checkpoint = context.add_or_update_checkpoint(
#     name="bigquery_checkpoint",
#     validations=[
#         {"batch_request": request, "expectation_suite_name": "my_suite"}
#     ],
# )
# checkpoint_result = checkpoint.run()
# print(checkpoint_result.get_statistics())
# print(checkpoint_result.list_validation_results())

# -- build html report and save to GCS
# context.build_data_docs(site_names="gs_site")