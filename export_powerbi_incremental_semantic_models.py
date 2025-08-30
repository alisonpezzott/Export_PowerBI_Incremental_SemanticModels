# Run if not installed
# pip install -U pyfabricops 

import pyfabricops as pf

pf.set_auth_provider('oauth') 
pf.setup_logging(format_style='minimal')  

pf.export_semantic_model(
    'WS_Demo',
    'Production',
    '.',
)

pf.export_report(
    'WS_Demo',
    'Production',
    '.',
)

pf.convert_report_definition_to_by_path(
    './Production.Report',
    '.',
)
