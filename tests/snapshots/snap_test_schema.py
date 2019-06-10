# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['APITestCase::test_catalog_all_fields 1'] = {
    'catalogList': {
        'edges': [
            {
                'node': {
                    'catalogId': 855,
                    'catalogName': 'Y1A1 COSMOS D04',
                    'description': 'A subset of Y1A1_COADD coadds in the COSMOS field. Coadds built to depth of 4 tilings, consistent with Year 1 depth.',
                    'flagRemoved': False,
                    'ingestionDate': '2016-08-30T14:30:06.827053',
                    'numColumns': 587,
                    'numObjects': 313380,
                    'numTiles': 8,
                    'statusId': 1,
                    'table': {
                        'tableId': 46
                    },
                    'tableId': 46,
                    'userId': 133,
                    'version': '1',
                    'visibility': 1
                }
            },
            {
                'node': {
                    'catalogId': 893,
                    'catalogName': 'Y1A1 STRIPE82',
                    'description': 'A subset of Y1A1_COADD coadds in the Stripe82 region.',
                    'flagRemoved': False,
                    'ingestionDate': '2015-11-03T20:26:17.083609',
                    'numColumns': 587,
                    'numObjects': 12487566,
                    'numTiles': 334,
                    'statusId': 1,
                    'table': {
                        'tableId': 399
                    },
                    'tableId': 399,
                    'userId': 374,
                    'version': 'v1.6',
                    'visibility': 1
                }
            }
        ]
    }
}

snapshots['APITestCase::test_fields_all_fields 1'] = {
    'fieldsList': {
        'edges': [
            {
                'node': {
                    'discoveryDate': '2015-03-21',
                    'displayName': 'COSMOS D04',
                    'fieldId': 47,
                    'fieldName': 'Y1A1_COADD_COSMOS_D04',
                    'installDate': '2015-09-04',
                    'releaseDate': '2015-03-19',
                    'releaseTag': {
                        'tagId': 24
                    },
                    'releaseTagId': 24,
                    'startDate': '2015-10-19',
                    'status': True
                }
            },
            {
                'node': {
                    'discoveryDate': '2014-10-10',
                    'displayName': 'STRIPE82',
                    'fieldId': 40,
                    'fieldName': 'Y1A1_COADD_STRIPE82',
                    'installDate': '2015-09-05',
                    'releaseDate': '2014-10-10',
                    'releaseTag': {
                        'tagId': 24
                    },
                    'releaseTagId': 24,
                    'startDate': '2015-11-03',
                    'status': True
                }
            },
            {
                'node': {
                    'discoveryDate': '2018-08-27',
                    'displayName': 'Y3 Gold Small',
                    'fieldId': 64,
                    'fieldName': 'Y3_GOLD',
                    'installDate': '2018-08-27',
                    'releaseDate': '2018-08-27',
                    'releaseTag': {
                        'tagId': 24
                    },
                    'releaseTagId': 24,
                    'startDate': '2018-08-27',
                    'status': True
                }
            }
        ]
    }
}

snapshots['APITestCase::test_filters_all_fields 1'] = {
    'filtersList': {
        'edges': [
            {
                'node': {
                    'filter': 'u',
                    'id': 'RmlsdGVyczp1',
                    'lambdaMax': 409.0,
                    'lambdaMean': 354.5,
                    'lambdaMin': 300.0
                }
            },
            {
                'node': {
                    'filter': 'g',
                    'id': 'RmlsdGVyczpn',
                    'lambdaMax': 557.0,
                    'lambdaMean': 474.0,
                    'lambdaMin': 391.0
                }
            },
            {
                'node': {
                    'filter': 'r',
                    'id': 'RmlsdGVyczpy',
                    'lambdaMax': 733.0,
                    'lambdaMean': 645.5,
                    'lambdaMin': 558.0
                }
            },
            {
                'node': {
                    'filter': 'i',
                    'id': 'RmlsdGVyczpp',
                    'lambdaMax': 885.0,
                    'lambdaMean': 783.5,
                    'lambdaMin': 682.0
                }
            },
            {
                'node': {
                    'filter': 'z',
                    'id': 'RmlsdGVyczp6',
                    'lambdaMax': 1026.0,
                    'lambdaMean': 926.0,
                    'lambdaMin': 826.0
                }
            }
        ]
    }
}

snapshots['APITestCase::test_group_pypelines_all_fields 1'] = {
    'groupPypelinesList': {
        'edges': [
            {
                'node': {
                    'displayName': 'Hidden',
                    'groupId': 43,
                    'name': 'hidden',
                    'orderNumber': 10000,
                    'parentGroup': None,
                    'parentGroupId': None
                }
            },
            {
                'node': {
                    'displayName': 'Catalog Production',
                    'groupId': 13,
                    'name': 'catalog_production',
                    'orderNumber': 30200,
                    'parentGroup': {
                        'groupId': 43
                    },
                    'parentGroupId': 43
                }
            },
            {
                'node': {
                    'displayName': 'Science Analysis',
                    'groupId': 29,
                    'name': 'science',
                    'orderNumber': 22000,
                    'parentGroup': None,
                    'parentGroupId': None
                }
            },
            {
                'node': {
                    'displayName': 'Simulation',
                    'groupId': 55,
                    'name': 'simulation',
                    'orderNumber': 40600,
                    'parentGroup': {
                        'groupId': 29
                    },
                    'parentGroupId': 29
                }
            },
            {
                'node': {
                    'displayName': 'Correlation',
                    'groupId': 33,
                    'name': 'correlation',
                    'orderNumber': 40610,
                    'parentGroup': {
                        'groupId': 55
                    },
                    'parentGroupId': 55
                }
            }
        ]
    }
}

snapshots['APITestCase::test_map_all_fields 1'] = {
    'mapList': {
        'edges': [
            {
                'node': {
                    'date': '2019-03-22T10:16:00',
                    'fieldId': 64,
                    'filter': '',
                    'flagRemoved': False,
                    'image': None,
                    'magnitude': None,
                    'mapId': 9809,
                    'nside': 4096,
                    'ordering': 'ring',
                    'snr': None,
                    'table': {
                        'tableId': 13915
                    },
                    'tableId': 13915,
                    'tag': {
                        'tagId': 33
                    },
                    'tagId': 33,
                    'type': None
                }
            },
            {
                'node': {
                    'date': '2019-03-22T09:42:00',
                    'fieldId': 64,
                    'filter': 'g',
                    'flagRemoved': False,
                    'image': None,
                    'magnitude': None,
                    'mapId': 9808,
                    'nside': 4096,
                    'ordering': 'ring',
                    'snr': None,
                    'table': {
                        'tableId': 13913
                    },
                    'tableId': 13913,
                    'tag': {
                        'tagId': 33
                    },
                    'tagId': 33,
                    'type': None
                }
            }
        ]
    }
}

snapshots['APITestCase::test_mask_all_fields 1'] = {
    'maskList': {
        'edges': [
            {
                'node': {
                    'date': '2019-03-18T00:00:00',
                    'field': {
                        'fieldId': 47
                    },
                    'fieldId': 47,
                    'filter': '',
                    'flagRemoved': False,
                    'maskId': 51,
                    'table': {
                        'tableId': 13101
                    },
                    'tableId': 13101,
                    'tag': {
                        'tagId': 24
                    },
                    'tagId': 24
                }
            }
        ]
    }
}

snapshots['APITestCase::test_modules_all_fields 1'] = {
    'modulesList': {
        'edges': [
            {
                'node': {
                    'description': None,
                    'displayName': 'Catalog Installation',
                    'grade': None,
                    'moduleId': 396,
                    'name': 'install_catalogs',
                    'pipelinesModules': {
                        'edges': [
                            {
                                'node': {
                                    'pipelineId': 174
                                }
                            }
                        ]
                    },
                    'user': {
                        'userId': 1
                    },
                    'userId': 1,
                    'version': 'V00_06_33',
                    'versionDate': '2016-01-18T16:49:01',
                    'xmlConfig': '''<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="/static/xml/mkform.xsl"?>
<config version="001" module="install_catalogs">
  <section id="Install Catalogs">
    <subsection id="Basic setup">
      <scalar default="No" type="string" name="Force overwrite" id="force_overwrite">
        <values>
          <value>No</value>
          <value>Yes</value>
        </values>
      </scalar>
    </subsection>
  </section>
</config>
'''
                }
            },
            {
                'node': {
                    'description': None,
                    'displayName': 'LePhare',
                    'grade': None,
                    'moduleId': 255,
                    'name': 'lephare_new',
                    'pipelinesModules': {
                        'edges': [
                            {
                                'node': {
                                    'pipelineId': 176
                                }
                            }
                        ]
                    },
                    'user': {
                        'userId': 1
                    },
                    'userId': 1,
                    'version': 'V07_00_09',
                    'versionDate': '2018-09-04T17:45:15.523132',
                    'xmlConfig': '''<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="/static/xml/mkform.xsl"?>
<config version="001" module="lephare_new">
  <section id="Photo-z handling">
    <subsection id="Fixed input redshift (Attention to previous run)">
      <scalar default="NO" type="string" name="Fix input redshift and search best model" id="ZFIX">
        <values>
          <value value="YES">Yes</value>
          <value value="NO">No</value>
        </values>
      </scalar>
      <scalar default="annz" type="string" name="Code to provide z" id="CODEFIX">
        <values>
          <value value="annz">annz</value>
          <value value="annz2">annz2</value>
          <value value="arborz">arborz</value>
          <value value="mlz">mlz</value>
        </values>
      </scalar>
    </subsection>
  </section>
  <section id="CREATION OF LIBRARIES FROM SEDs List">
    <subsection id="STELLAR LIBRARY">
      <scalar default="$LEPHAREDIR/sed/STAR/STAR_MOD.list" hidden="hidden" type="string" name="" id="STAR_SED">
        <values>
          <value>$LEPHAREDIR/sed/STAR/STAR_MOD.list</value>
        </values>
      </scalar>
      <scalar default="3.432E-09" type="string" name="Star flux scale" id="STAR_FSCALE">
        <values>
          <value>3.432E-09</value>
        </values>
      </scalar>
      <scalar default="LIB_STAR" hidden="hidden" type="string" name="" id="STAR_LIB">
        <values>
          <value>LIB_STAR</value>
        </values>
      </scalar>
    </subsection>
    <subsection id="QSO LIBRARY">
      <scalar default="$LEPHAREDIR/sed/QSO/QSO_MOD_MIX.list" hidden="hidden" type="string" name="" id="QSO_SED">
        <values>
          <value>$LEPHAREDIR/sed/QSO/QSO_MOD.list</value>
        </values>
      </scalar>
      <scalar default="1.0" type="float" name="QSO flux scale" id="QSO_FSCALE">
        <values>
          <value>1.0</value>
        </values>
      </scalar>
      <scalar default="LIB_QSO" hidden="hidden" type="string" name="" id="QSO_LIB">
        <values>
          <value>LIB_QSO</value>
        </values>
      </scalar>
    </subsection>
    <subsection id="GALAXY LIBRARY">
      <scalar default="CFHTLS_MOD31.list" type="string" name="SED set for galaxies" id="GAL_SED">
        <values>
          <value value="CWW_MOD.list2">CWW</value>
          <value value="CFHTLS_MOD43.list">CFHTLS_18</value>
          <value value="CFHTLS_MOD31.list">CFHTLS_21</value>
          <value disabled="disabled" value="/sed/GAL/CFHTLS_SED/CFHTLS_MOD.list">CFHTLS (66 SEDs)</value>
          <value disabled="disabled" value="sed/GAL/CFHTLS_SED/CFHTLS_MOD14.list">CFHTLS (31 SEDs, no starburst)</value>
          <value disabled="disabled" value="/sed/GAL/PEGASE2/PEGASE2_MOD.list">PEGASE2</value>
        </values>
      </scalar>
      <scalar default="1.0" type="float" name="Galaxy flux scale" id="GAL_FSCALE">
        <values>
          <value>1.0</value>
        </values>
      </scalar>
      <scalar default="LIB_CFHT21SED" hidden="hidden" type="string" name="" id="GAL_LIB">
        <values>
          <value>LIB_CFHT21SED</value>
        </values>
      </scalar>
      <!--<scalar id="SEL_AGE" name="" type="string" default="$LEPHAREDIR/sed/GAL/HYPERZ/AGE_GISSEL_ALL.dat" hidden="hidden"><values><value>$LEPHAREDIR/sed/GAL/HYPERZ/AGE_GISSEL_ALL.dat</value></values></scalar>-->
      <list type="float" name="Age Min-Max in yr" id="AGE_RANGE">
        <values>
          <value>0.</value>
          <value>13.e9</value>
        </values>
      </list>
    </subsection>
    <!--subsection id="Object Selection"><scalar default="YES" id="GALS_ONLY" name="Select only true galaxies" type="string"><values><value>YES</value><value>NO</value></values></scalar></subsection-->
    <!--subsection id="Ingest Catalog"><scalar default="no" id="Ingestion" name="Ingest table in Database?" type="string"><values><value>yes</value><value>no</value></values></scalar><scalar default="no" id="Parallel" name="Ingest in parallel?" type="string"><values><value>yes</value><value>no</value></values></scalar></subsection-->
  </section>
  <section id="Filters">
    <subsection>
      <scalar default="AUTO" type="string" name="Photometric type" id="photo_type">
        <values>
          <value>simulation</value>
          <value>AUTO</value>
          <value>APER_3</value>
          <value>APER_4</value>
          <value>MODEL</value>
          <value>DETMODEL</value>
        </values>
      </scalar>
      <list type="string" name="Filter list" id="FILTER_LIST">
        <values>
          <value>g</value>
          <value>r</value>
          <value>i</value>
          <value>z</value>
          <value>Y</value>
        </values>
      </list>
      <scalar default="0" type="int" name="Transmission type" id="TRANS_TYPE">
        <values>
          <value value="0">Energy</value>
          <value value="1">Number of photons</value>
        </values>
      </scalar>
      <scalar default="0" hidden="hidden" type="int" name="" id="FILTER_CALIB">
        <values>
          <value value="0">fnu=ctt</value>
          <value value="1">nu.fnu=ctt</value>
          <value value="2">fnu=nu</value>
          <value value="3">fnu=Black Body</value>
          <value value="4">for MIPS</value>
        </values>
      </scalar>
      <scalar default="filters.dat" hidden="hidden" type="string" name="" id="FILTER_FILE">
        <values>
          <value>filters.dat</value>
        </values>
      </scalar>
    </subsection>
  </section>
  <section id="THEORETICAL MAGNITUDES">
    <subsection>
      <scalar default="LIB_STAR" hidden="hidden" type="string" name="" id="STAR_LIB_IN">
        <values>
          <value>LIB_STAR</value>
        </values>
      </scalar>
      <scalar default="STAR_MAG" hidden="hidden" type="string" name="" id="STAR_LIB_OUT">
        <values>
          <value>STAR_MAG</value>
        </values>
      </scalar>
      <scalar default="LIB_QSO" hidden="hidden" type="string" name="" id="QSO_LIB_IN">
        <values>
          <value>LIB_QSO</value>
        </values>
      </scalar>
      <scalar default="QSO_MAG" hidden="hidden" type="string" name="" id="QSO_LIB_OUT">
        <values>
          <value>QSO_MAG</value>
        </values>
      </scalar>
      <scalar default="LIB_CFHT21SED" hidden="hidden" type="string" name="" id="GAL_LIB_IN">
        <values>
          <value>LIB_CFHT21SED</value>
        </values>
      </scalar>
      <scalar default="CFHT21SED_MAG" hidden="hidden" type="string" name="" id="GAL_LIB_OUT">
        <values>
          <value>CFHT21SED_MAG</value>
        </values>
      </scalar>
      <scalar default="AB" type="string" name="Magnitude type" id="MAGTYPE">
        <values>
          <value>AB</value>
          <value>VEGA</value>
        </values>
      </scalar>
      <list type="float" name="Redshift: step, maximum, new step if maximum 6" id="Z_STEP">
        <values>
          <value>0.02</value>
          <value>3</value>
          <value>0.1</value>
        </values>
      </list>
      <list type="float" name="H0, density parameters: matter and lambda" id="COSMOLOGY">
        <values>
          <value>67.8</value>
          <value>0.308</value>
          <value>0.692</value>
        </values>
      </list>
      <list type="int" name="Model range for extinction" id="MOD_EXTINC">
        <values>
          <value>15</value>
          <value>21</value>
        </values>
      </list>
      <scalar default="SB_calzetti.dat" type="string" name="Extinction law" id="EXTINC_LAW">
        <values>
          <value value="NONE">NONE</value>
          <value value="LMC_Fitzpatrick.dat">LMC_Fitzpatrick</value>
          <value value="MW_Allen.dat">MW_Allen</value>
          <value value="MW_seaton.dat">MW_Seaton</value>
          <value value="SB_calzetti.dat">SB_Calzetti</value>
          <value value="SMC_prevot.dat">SMC_Prevot</value>
        </values>
      </scalar>
      <list type="float" name="E(B-V) list" id="EB_V">
        <values>
          <value>0.0</value>
          <value>0.05</value>
          <value>0.1</value>
          <value>0.15</value>
          <value>0.2</value>
          <value>0.25</value>
        </values>
      </list>
      <scalar default="NO" type="string" name="EM_LINES" id="EM_LINES">
        <values>
          <value value="YES">y</value>
          <value value="NO">n</value>
        </values>
      </scalar>
      <!--list id="Z_FORM" name="Formation z for each SED" type="int" hidden="hidden">Duvida que valor atribuir se nao quiser que seja usado<values><value>0</value></values></list-->
      <scalar default="YES" hidden="hidden" type="string" name="Write output in ASCII" id="LIB_ASCII">
        <values>
          <value value="YES">y</value>
          <value value="NO">n</value>
        </values>
      </scalar>
    </subsection>
  </section>
  <section id="PHOTOMETRIC REDSHIFTS">
    <subsection id="Input Catalog Informations">
      <scalar default="LEPHAREDIR/test/hdfn_lanzetta.in" hidden="hidden" type="string" name="Input catalog" id="CAT_IN">
        <values>
          <value>$LEPHAREDIR/test/hdfn_lanzetta.in</value>
        </values>
      </scalar>
      <scalar default="M" type="string" name="Input type" id="INP_TYPE">
        <values>
          <value value="M">Magnitude</value>
          <value value="F">Flux</value>
        </values>
      </scalar>
      <scalar default="AB" type="string" name="Input magnitude" id="CAT_MAG">
        <values>
          <value>AB</value>
          <value>VEGA</value>
        </values>
      </scalar>
      <scalar default="MEME" hidden="hidden" type="string" name="CAT_FMT" id="CAT_FMT">
        <values>
          <value>MEME</value>
          <value>MMEE</value>
        </values>
      </scalar>
      <list default="-99,-99" type="int" name="MIN and MAX RANGE of ROWS used in input cat" id="CAT_LINES">
        <values>
          <value>-99</value>
          <value>-99</value>
        </values>
      </list>
      <scalar default="LONG" hidden="hidden" type="string" name="Input format" id="CAT_TYPE">
        <values>
          <value>LONG</value>
          <value>SHORT</value>
        </values>
      </scalar>
      <scalar default="0" hidden="hidden" type="int" name="Bands used for scaling" id="BD_SCALE">
        <values>
          <value>0</value>
        </values>
      </scalar>
      <scalar default="-1" type="int" name="Global context" id="GLB_CONTEXT">
        <values>
          <value>-1</value>
        </values>
      </scalar>
      <!--list id="ERR_SCALE" name="" type="float" hidden="hidden"><values><value>0.0</value></values></list-->
      <scalar default="1.5" type="float" name="Error scaling factor" id="ERR_FACTOR">
        <values>
          <value>1.5</value>
        </values>
      </scalar>
    </subsection>
    <subsection id="Theoretical libraries">
      <list hidden="hidden" type="string" name="Libraries" id="ZPHOTLIB">
        <values>
          <value>CFHT21SED</value>
          <value>STAR_MAG</value>
          <value>QSO_MAG</value>
        </values>
      </list>
      <scalar default="NO" type="string" name="ADD_EMLINES" id="ADD_EMLINES">
        <values>
          <value value="YES">y</value>
          <value value="NO">n</value>
        </values>
      </scalar>
    </subsection>
    <subsection>
      <!--id="Output catalog Name" hidden="hidden"-->
      <scalar default="$LEPHAREDIR/test/zphot.out" hidden="hidden" type="string" name="Output catalog" id="CAT_OUT">
        <values>
          <value>$LEPHAREDIR/zphot.out</value>
        </values>
      </scalar>
      <scalar default="zphot_vac.para" hidden="hidden" type="string" name="Output parameters" id="PARA_OUT">
        <values>
          <!--value>$LEPHAREDIR/zphot_output.para</value-->
          <value>zphot_vac.para</value>
        </values>
      </scalar>
    </subsection>
    <subsection>
      <!--Infrared-->
      <scalar default="NONE" hidden="hidden" type="string" name="FIR_LIB" id="FIR_LIB">
        <values>
          <value>NONE</value>
        </values>
      </scalar>
      <scalar default="7.0" hidden="hidden" type="float" name="FIR_LMIN" id="FIR_LMIN">
        <values>
          <value>7.0</value>
        </values>
      </scalar>
      <scalar default="-1" hidden="hidden" type="int" name="FIR_LMIN" id="FIR_CONT">
        <values>
          <value>-1</value>
        </values>
      </scalar>
      <scalar default="-1" hidden="hidden" type="int" name="FIR_SCALE" id="FIR_SCALE">
        <values>
          <value>-1</value>
        </values>
      </scalar>
      <scalar default="YES" hidden="hidden" type="string" name="FIR_FREESCALE" id="FIR_FREESCALE">
        <values>
          <value value="YES">y</value>
          <value value="NO">n</value>
        </values>
      </scalar>
      <scalar default="NO" hidden="hidden" type="string" name="FIR_SUBSTELLAR" id="FIR_SUBSTELLAR">
        <values>
          <value value="YES">y</value>
          <value value="NO">n</value>
        </values>
      </scalar>
      <scalar default="NONE" hidden="hidden" type="string" name="PHYS_LIB" id="PHYS_LIB">
        <values>
          <value>NONE</value>
        </values>
      </scalar>
      <scalar default="-1" hidden="hidden" type="int" name="PHYS_LMIN" id="PHYS_CONT">
        <values>
          <value>-1</value>
        </values>
      </scalar>
      <scalar default="-1" hidden="hidden" type="int" name="PHYS_SCALE" id="PHYS_SCALE">
        <values>
          <value>-1</value>
        </values>
      </scalar>
      <scalar default="100000" hidden="hidden" type="int" name="PHYS_SCALE" id="PHYS_NMAX">
        <values>
          <value>100000</value>
        </values>
      </scalar>
    </subsection>
    <subsection id="Priors">
      <list hidden="hidden" type="float" name="" id="MASS_SCALE">
        <values>
          <value>0.0</value>
          <value>0.0</value>
        </values>
      </list>
      <list type="float" name="Absolute magnitude: minimum and maximum" id="MAG_ABS">
        <values>
          <value>-10.</value>
          <value>-26.</value>
        </values>
      </list>
      <scalar default="4" type="int" name="Reference number for band used in absolute mag limits" id="MAG_REF">
        <values>
          <value>4</value>
        </values>
      </scalar>
      <!--list id="ZFORM_MIN" name="" type="float" hidden="hidden"><values><value>0.0</value></values></list-->
      <list type="float" name="Z min-max used for the Galaxy library" id="Z_RANGE">
        <values>
          <value>0.</value>
          <value>99.99</value>
        </values>
      </list>
      <list type="int" name="E(B-V) MIN-MAX RANGE of E(B-V) used" id="EBV_RANGE">
        <values>
          <value>0</value>
          <value>9</value>
        </values>
      </list>
      <!--scalar id="ZMAX_GAL" name="Maximum z used for the Galaxy library" type="float" default="99.99"><values><value>99.99</value></values></scalar-->
      <list type="int" name="I band for prior on N(z)" id="NZ_PRIOR">
        <values>
          <value>3</value>
          <value>1</value>
          <value>3</value>
        </values>
      </list>
    </subsection>
    <subsection id="Parabolic interpolation for Zbest">
      <scalar default="YES" type="string" name="Redshift interpolation" id="Z_INTERP">
        <values>
          <value value="YES">y</value>
          <value value="NO">n</value>
        </values>
      </scalar>
    </subsection>
    <subsection id="Analysis of normalized ML curve - Secondary peak analysis">
      <description>ML(exp-(0.5*χ²))</description>
      <scalar default="0.5" type="float" name="Window search for 2nd peaks" id="DZ_WIN">
        <values>
          <value>0.5</value>
        </values>
      </scalar>
      <scalar default="0.1" type="float" name="Lower threshold for 2nd peaks" id="MIN_THRES">
        <values>
          <value>0.1</value>
        </values>
      </scalar>
    </subsection>
    <!--subsection id="Probability (in %) per redshift intervals"><list id="PROB_INTZ" name="Redshift bins" type="float" hidden="hidden"><values><value>0.0</value></values></list></subsection-->
    <subsection id="ABSOLUTE MAGNITUDES COMPUTATION">
      <scalar default="0" type="int" name="Method" id="MABS_METHOD">
        <values>
          <value value="0">obs- Ref</value>
          <value value="1">best obs- Ref</value>
          <value value="2">fixed obs- Ref</value>
          <value value="3">mag from best SED</value>
          <value value="4">z bin</value>
        </values>
      </scalar>
      <scalar default="-1" type="int" name="Context for Band used for MABS" id="MABS_CONTEXT">
        <values>
          <value>-1</value>
        </values>
      </scalar>
      <scalar default="4" type="int" name="Filter obs chosen for absolute mag (only for method=fixed obs- Ref)" id="MABS_REF">
        <values>
          <value>4</value>
        </values>
      </scalar>
      <list type="int" name="Chosen filters per z bin (only for method=z bin)" id="MABS_FILT">
        <values>
          <value>1</value>
          <value>2</value>
          <value>3</value>
          <value>4</value>
        </values>
      </list>
      <list type="float" name="Redshift bins (only for method=z bin)" id="MABS_ZBIN">
        <values>
          <value>0</value>
          <value>0.5</value>
          <value>1</value>
          <value>1.5</value>
          <value>2</value>
          <value>3</value>
          <value>3.5</value>
          <value>4</value>
        </values>
      </list>
    </subsection>
    <subsection>
      <!--id="OUTPUT SPECTRA"-->
      <scalar default="NO" hidden="hidden" type="string" name="Spectrum for each object" id="SPEC_OUT">
        <values>
          <value value="YES">y</value>
          <value value="NO">n</value>
        </values>
      </scalar>
      <list hidden="hidden" type="int" name="MABS for REF FILTERS to be extracted" id="PDZ_MABS_FILT">
        <values>
          <value>2</value>
          <value>10</value>
          <value>14</value>
        </values>
      </list>
    </subsection>
    <subsection>
      <!--id="OUTPUT PDZ ANALYSIS"-->
      <scalar default="NONE" hidden="hidden" type="string" name="pdz output file name" id="PDZ_OUT">
        <values>
          <value value="NONE">NONE</value>
        </values>
      </scalar>
      <scalar default="NO" hidden="hidden" type="string" name="output file with all values : z,mod,chi2,E(B-V)" id="CHI2_OUT">
        <values>
          <value value="YES">y</value>
          <value value="NO">n</value>
        </values>
      </scalar>
    </subsection>
    <subsection id="FAST MODE: color-space reduction">
      <scalar default="NO" type="string" name="Fast computation" id="FAST_MODE">
        <values>
          <value value="YES">y</value>
          <value value="NO">n</value>
        </values>
      </scalar>
      <scalar default="3" type="int" name="Number of colors used" id="COL_NUM">
        <values>
          <value>3</value>
        </values>
      </scalar>
      <scalar default="3.0" type="float" name="Enlarge of the obs. color errors" id="COL_SIGMA">
        <values>
          <value>3.0</value>
        </values>
      </scalar>
      <scalar default="AND" type="string" name="Combination between used colors" id="COL_SEL">
        <values>
          <value>AND</value>
          <value>OR</value>
        </values>
      </scalar>
    </subsection>
    <subsection id="Magnitude shifts applied to libraries">
      <list type="float" name="Systematic shifts to be applied in each band" id="APPLY_SYSSHIFT">
        <values>
          <value>0.0</value>
          <value>0.0</value>
          <value>0.0</value>
          <value>0.0</value>
          <value>0.0</value>
        </values>
      </list>
    </subsection>
    <!--subsection id="ADAPTIVE METHOD using Z spectro sample"><scalar id="AUTO_ADAPT" name="Adapting method with spectrum (NOT IN USE)" type="string" default="NO"><values><value value="YES">y</value><value value="NO">n</value></values></scalar><list id="ADAPT_BAND" name="Reference band, 1st and 2nd bands for color" type="int"><values><value>4</value><value>2</value><value>4</value></values></list><list id="ADAPT_LIM" name="Mag limits for spectrum in Ref band" type="float"><values><value>13.0</value><value>28.0</value></values></list><scalar id="ADAPT_POLY" name="Number of coeficients in polynom" type="int" default="1"><values><value>1</value><value>2</value><value>3</value><value>4</value></values></scalar><scalar id="ADAPT_METH" name="Fit as a function of" type="int" default="1"><values><value value="1">color model</value><value value="2">redshift</value><value value="3">models</value></values></scalar><scalar id="ADAPT_CONTEXT" name="Context for bands used for training" type="int" default="-1"><values><value>-1</value></values></scalar><list id="ADAPT_ZBIN" name="Redshift\'s interval used for training" type="float"><values><value>0.01</value><value>6.0</value></values></list><list id="ADAPT_MODBIN" name="Model\'s interval used for training" type="int"><values><value>1</value><value>1000</value></values></list><scalar id="ERROR_ADAPT" name="Add error in quadrature" type="string" default="NO"><values><value value="YES">y</value><value value="NO">n</value></values></scalar></subsection><subsection id="COLOR METHOD for &#967;&#178; minimisation"><list id="C17_METHOD" type="int" ><values><value>2</value><value>3</value><value>5</value><value>-1</value></values></list></subsection-->
  </section>
</config>
'''
                }
            },
            {
                'node': {
                    'description': None,
                    'displayName': 'DNF',
                    'grade': None,
                    'moduleId': 480,
                    'name': 'dnf',
                    'pipelinesModules': {
                        'edges': [
                            {
                                'node': {
                                    'pipelineId': 176
                                }
                            }
                        ]
                    },
                    'user': {
                        'userId': 1
                    },
                    'userId': 1,
                    'version': 'V03_03_14',
                    'versionDate': '2018-09-04T17:45:15.523132',
                    'xmlConfig': None
                }
            }
        ]
    }
}

snapshots['APITestCase::test_nested_sort 1'] = {
    'productClassList': {
        'edges': [
            {
                'node': {
                    'displayName': 'Astrometry Outliers',
                    'productType': {
                        'displayName': 'Targets',
                        'typeId': 1
                    },
                    'typeId': 1
                }
            },
            {
                'node': {
                    'displayName': 'Cluster Members',
                    'productType': {
                        'displayName': 'Targets',
                        'typeId': 1
                    },
                    'typeId': 1
                }
            },
            {
                'node': {
                    'displayName': 'Color Outliers',
                    'productType': {
                        'displayName': 'Targets',
                        'typeId': 1
                    },
                    'typeId': 1
                }
            },
            {
                'node': {
                    'displayName': 'Galaxy Clusters',
                    'productType': {
                        'displayName': 'Targets',
                        'typeId': 1
                    },
                    'typeId': 1
                }
            },
            {
                'node': {
                    'displayName': 'Matched Clusters',
                    'productType': {
                        'displayName': 'Targets',
                        'typeId': 1
                    },
                    'typeId': 1
                }
            }
        ]
    }
}

snapshots['APITestCase::test_pipeline_stage_all_fields 1'] = {
    'pipelineStageList': {
        'edges': [
            {
                'node': {
                    'displayName': 'Data Installation',
                    'level': 1,
                    'name': 'data_installation',
                    'pipelineStageId': 1
                }
            },
            {
                'node': {
                    'displayName': 'Data Preparation',
                    'level': 2,
                    'name': 'data_preparation',
                    'pipelineStageId': 4
                }
            },
            {
                'node': {
                    'displayName': 'Simulations',
                    'level': 4,
                    'name': 'simulations',
                    'pipelineStageId': 7
                }
            },
            {
                'node': {
                    'displayName': 'Utilities',
                    'level': 5,
                    'name': 'utilities',
                    'pipelineStageId': 8
                }
            },
            {
                'node': {
                    'displayName': 'Special Samples',
                    'level': 7,
                    'name': 'special_samples',
                    'pipelineStageId': 10
                }
            },
            {
                'node': {
                    'displayName': 'Science-Ready Catalogs',
                    'level': 3,
                    'name': 'valueadded_catalog',
                    'pipelineStageId': 5
                }
            },
            {
                'node': {
                    'displayName': 'Science Analysis',
                    'level': 6,
                    'name': 'science',
                    'pipelineStageId': 9
                }
            }
        ]
    }
}

snapshots['APITestCase::test_pipelines_all_fields 1'] = {
    'pipelinesList': {
        'edges': [
            {
                'node': {
                    'anyOutputClass': False,
                    'description': 'This pipeline finds clusters of galaxies using WAZP',
                    'displayName': 'WAZP',
                    'group': {
                        'groupId': 52
                    },
                    'groupId': 52,
                    'multidataset': False,
                    'name': 'wazp_new',
                    'orderNumber': 120,
                    'pipelineId': 214,
                    'pipelineStage': {
                        'pipelineStageId': 9
                    },
                    'pipelineStageId': 9,
                    'pipelineStatus': {
                        'pipelineStatusId': 1
                    },
                    'pipelineStatusId': 1,
                    'processes': [
                        {
                            'processId': 10031073
                        }
                    ],
                    'readme': None,
                    'user': {
                        'userId': 1
                    },
                    'userId': 1,
                    'version': 'V01_05_01',
                    'versionDate': '2018-07-16T16:19:49',
                    'xmlWorkflow': '''<?xml version="1.0" encoding="UTF-8"?>
<pipeline name="WAZP">
  <info>
    <group value="cluster"/>
    <stage value="science"/>
    <owner value="ogando"/>
    <description>This pipeline finds clusters of galaxies using WAZP</description>
  </info>
  <taskgroup id="slice" desc="WAZP Components">
    <task checked="checked" name="Slicing" flow="1to1" confName="Slicing" config="yes" id="wazp_slice_zmag">
      <components>
        <component name="Slicing" id="wazp_slice_zmag"/>
      </components>
      <dependencies>
        <dependency id="scienceportal">
          <file mimetype="text/xml" source="scienceportal" class="pype_input" value="pype_input.xml"/>
        </dependency>
      </dependencies>
    </task>
    <task checked="checked" name="Split Area" flow="1toN" confName="Tiling" config="no" id="wazp_split_area">
      <components>
        <component name="Split Area" id="wazp_split_area"/>
      </components>
      <dependencies>
        <dependency id="scienceportal">
          <file mimetype="text/xml" source="scienceportal" class="pype_input" value="pype_input.xml"/>
        </dependency>
        <dependency id="wazp_slice_zmag">
          <file mimetype="text/plain" optional="True" class="wazp_config"/>
          <config type="string" optional="True" id="vac_class"/>
        </dependency>
      </dependencies>
    </task>
    <task checked="checked" name="Visibility Maps" flow="1to1" confName="Visibility maps" config="no" id="wazp_visibility_maps">
      <components>
        <component name="Visibility Maps" id="wazp_visibility_maps"/>
      </components>
      <dependencies>
        <dependency id="scienceportal">
          <file mimetype="text/xml" source="scienceportal" class="pype_input" value="pype_input.xml"/>
        </dependency>
        <dependency id="wazp_slice_zmag">
          <file mimetype="text/plain" optional="True" class="calib_zmag_slice"/>
          <file mimetype="text/plain" optional="True" class="wazp_config"/>
          <config type="string" optional="True" id="vac_class"/>
        </dependency>
        <dependency id="wazp_split_area">
          <file mimetype="text/plain" optional="True" class="tile_vertices"/>
          <file mimetype="text/plain" optional="True" class="footprint_txt"/>
          <!--file mimetype="application/fits-table" class="vac_cluster" optional="True"/-->
        </dependency>
      </dependencies>
    </task>
    <task checked="checked" name="Background modelling per tile" flow="1to1" confName="Background" config="no" id="wazp_bkg_model">
      <components>
        <component name="Background modelling per tile" id="wazp_bkg_model"/>
      </components>
      <dependencies>
        <dependency id="wazp_slice_zmag">
          <file mimetype="text/plain" optional="True" class="calib_zmag_slice"/>
          <file mimetype="text/plain" optional="True" class="wazp_config"/>
          <config type="string" optional="True" id="vac_class"/>
        </dependency>
        <dependency id="wazp_split_area">
          <file mimetype="text/plain" optional="True" class="tile_vertices"/>
          <!--file mimetype="application/fits-table" class="vac_cluster" optional="True"/-->
        </dependency>
        <dependency id="wazp_visibility_maps">
          <file mimetype="application/fits-table" optional="True" class="visibility_map_trim"/>
          <file mimetype="application/fits-table" optional="True" class="vac_cluster"/>
        </dependency>
      </dependencies>
    </task>
    <task checked="checked" name="Background concatenation" flow="Nto1" confName="Background" config="no" id="wazp_bkg_concat">
      <components>
        <component name="Background concatenation" id="wazp_bkg_concat"/>
      </components>
      <dependencies>
        <dependency id="wazp_slice_zmag">
          <file mimetype="text/plain" optional="True" class="calib_zmag_slice"/>
          <file mimetype="text/plain" optional="True" class="wazp_config"/>
          <config type="string" optional="True" id="vac_class"/>
        </dependency>
        <dependency id="wazp_split_area">
          <file mimetype="text/plain" class="tiles_list" optiona="True"/>
        </dependency>
        <dependency id="wazp_visibility_maps">
          <file mimetype="application/fits-table" optional="True" class="visibility_map_trim"/>
          <!-- file mimetype="application/fits-table" class="vac_cluster" optional="True"/-->
        </dependency>
        <dependency id="wazp_bkg_model">
          <file mimetype="application/x-tar" optional="True" class="bkg_model"/>
        </dependency>
      </dependencies>
    </task>
    <task checked="checked" name="WAZP split per tile" transfer="False" flow="1toN" display="hidden" confName="WAZP" config="no" id="wazp_pre_tile">
      <components>
        <component name="WAZP split per tile" id="wazp_pre_tile"/>
      </components>
      <dependencies>
        <dependency id="wazp_slice_zmag">
          <file mimetype="text/plain" optional="True" class="calib_zmag_slice"/>
          <file mimetype="text/plain" optional="True" class="wazp_config"/>
        </dependency>
        <dependency id="wazp_split_area">
          <file mimetype="text/plain" optional="True" class="tile_vertices"/>
          <!--file mimetype="application/fits-table" class="vac_cluster" optional="True"/-->
        </dependency>
        <dependency id="wazp_visibility_maps">
          <file mimetype="application/fits-table" optional="True" class="visibility_maps"/>
          <file mimetype="application/fits-table" optional="True" class="vac_cluster"/>
        </dependency>
        <dependency id="wazp_bkg_concat">
          <file mimetype="text/plain" optional="True" class="bkg_model"/>
          <file mimetype="text/plain" optional="True" class="bkg_model_mag"/>
        </dependency>
      </dependencies>
    </task>
    <task checked="checked" name="Cluster detection per tile" flow="1to1" confName="WAZP" config="no" id="wazp_tile">
      <components>
        <component name="Cluster detection per tile" id="wazp_tile"/>
      </components>
      <dependencies>
        <dependency id="wazp_slice_zmag">
          <file mimetype="text/plain" optional="True" class="calib_zmag_slice"/>
          <file mimetype="text/plain" optional="True" class="wazp_config"/>
          <config type="string" optional="True" id="vac_class"/>
        </dependency>
        <dependency id="wazp_split_area">
          <file mimetype="text/plain" optional="True" class="tile_vertices"/>
          <config type="string" optional="True" id="tile_max_area"/>
          <!--file mimetype="application/fits-table" class="vac_cluster" optional="True"/-->
        </dependency>
        <dependency id="wazp_visibility_maps">
          <file mimetype="application/fits-table" optional="True" class="visibility_maps"/>
          <file mimetype="application/fits-table" optional="True" class="vac_cluster"/>
        </dependency>
        <dependency id="wazp_bkg_concat">
          <file mimetype="text/plain" optional="True" class="bkg_model"/>
          <file mimetype="text/plain" optional="True" class="bkg_model_mag"/>
        </dependency>
      </dependencies>
    </task>
    <task checked="checked" config="no" flow="Nto1" name="Clusters concatenation" id="wazp_concatenate">
      <components>
        <component id="wazp_concatenate" multithreaded="True" name="Clusters concatenation"/>
      </components>
      <dependencies>
        <dependency id="scienceportal">
          <file mimetype="text/xml" source="scienceportal" class="pype_input" value="pype_input.xml"/>
        </dependency>
        <dependency id="wazp_slice_zmag">
          <file mimetype="text/plain" optional="True" class="wazp_config"/>
          <config type="string" optional="True" id="vac_area"/>
          <config type="string" optional="True" id="vac_class"/>
        </dependency>
        <dependency id="wazp_split_area">
          <file mimetype="text/plain" optional="True" class="tiles_list"/>
        </dependency>
        <dependency id="wazp_tile">
          <file mimetype="application/fits-table" optional="True" class="cluster_list"/>
          <file mimetype="application/fits-table" optional="True" class="member_list"/>
          <file mimetype="text/plain" optional="True" class="tile_coords"/>
          <file mimetype="image/png" optional="True" class="histo_zp"/>
          <file mimetype="image/png" optional="True" class="zph_mag"/>
        </dependency>
      </dependencies>
    </task>
  </taskgroup>
</pipeline>
'''
                }
            },
            {
                'node': {
                    'anyOutputClass': False,
                    'description': None,
                    'displayName': 'Install Catalogs',
                    'group': {
                        'groupId': 43
                    },
                    'groupId': 43,
                    'multidataset': False,
                    'name': 'install_catalogs',
                    'orderNumber': 600,
                    'pipelineId': 185,
                    'pipelineStage': {
                        'pipelineStageId': 1
                    },
                    'pipelineStageId': 1,
                    'pipelineStatus': {
                        'pipelineStatusId': 1
                    },
                    'pipelineStatusId': 1,
                    'processes': [
                        {
                            'processId': 10021032
                        },
                        {
                            'processId': 10024396
                        }
                    ],
                    'readme': None,
                    'user': {
                        'userId': 1
                    },
                    'userId': 1,
                    'version': 'V00_00_04',
                    'versionDate': '2016-04-06T10:16:48',
                    'xmlWorkflow': '''<?xml version="1.0" encoding="UTF-8"?>
<pipeline name="Install Catalogs">
  <info>
    <group value="hidden"/>
    <stage value="data_installation"/>
    <owner value="riccardo.campisano"/>
    <description/>
  </info>
  <taskgroup id="main" desc="Install Catalogs">
    <task checked="checked" config="yes" flow="1to1" name="Download" id="download_request">
      <components>
        <component name="Download Request" id="download_request"/>
      </components>
      <dependencies>
        <dependency id="scienceportal">
          <file mimetype="text/xml" source="scienceportal" class="pype_input" value="pype_input.xml"/>
          <config type="string" id="product" value="cats"/>
        </dependency>
      </dependencies>
    </task>
    <task checked="checked" config="yes" flow="1to1" name="Install" id="install_catalogs">
      <components>
        <component name="Catalog Installation" id="install_catalogs"/>
      </components>
      <dependencies>
        <dependency id="scienceportal">
          <file mimetype="text/xml" source="scienceportal" class="pype_input" value="pype_input.xml"/>
        </dependency>
      </dependencies>
    </task>
  </taskgroup>
</pipeline>
'''
                }
            },
            {
                'node': {
                    'anyOutputClass': False,
                    'description': 'Creates a catalog based on user configuration, joining all the input products and produces a log with the catalog characterization',
                    'displayName': 'Cluster',
                    'group': {
                        'groupId': 67
                    },
                    'groupId': 67,
                    'multidataset': False,
                    'name': 'vac_cluster',
                    'orderNumber': 949,
                    'pipelineId': 200,
                    'pipelineStage': {
                        'pipelineStageId': 5
                    },
                    'pipelineStageId': 5,
                    'pipelineStatus': {
                        'pipelineStatusId': 1
                    },
                    'pipelineStatusId': 1,
                    'processes': [
                    ],
                    'readme': None,
                    'user': {
                        'userId': 1
                    },
                    'userId': 1,
                    'version': 'V00_08_19',
                    'versionDate': '2018-07-19T14:05:23',
                    'xmlWorkflow': '''<?xml version="1.0" encoding="UTF-8"?>
<pipeline name="Cluster">
  <info>
    <group value="valueadded_catalog"/>
    <stage value="valueadded_catalog"/>
    <owner value="angelofausti"/>
    <description>Creates a catalog based on user configuration, joining all the input products and produces a log with the catalog characterization</description>
  </info>
  <taskgroup id="catalog" desc="Cluster Catalog">
    <task checked="checked" name="Query Builder" flow="1to1" confName="Catalog Definition" config="yes" id="query_builder">
      <components>
        <component name="Query Builder" id="query_builder"/>
      </components>
      <dependencies>
        <dependency id="scienceportal">
          <file mimetype="text/xml" source="scienceportal" class="pype_input" value="pype_input.xml"/>
        </dependency>
      </dependencies>
    </task>
    <task checked="checked" name="Catalog Properties" flow="1to1" confName="Catalog Properties" config="no" id="catalog_properties">
      <components>
        <component name="Catalog Properties" id="catalog_properties"/>
      </components>
      <dependencies>
        <dependency id="query_builder">
          <config type="string" id="table"/>
          <config type="string" id="tag"/>
          <config type="string" id="extinction"/>
          <config type="string" optional="True" id="photoz_method"/>
          <config type="string" id="color_cut_gr"/>
          <config type="string" id="color_cut_ri"/>
          <config type="string" id="color_cut_iz"/>
          <config type="string" id="color_cut_zY"/>
          <file mimetype="image/png" optional="True" class="vac"/>
          <config type="string" optional="True" id="zmax"/>
          <config type="float" optional="True" id="footprintarea"/>
          <config type="float" optional="True" id="nobjs"/>
          <config type="string" optional="True" id="mag_type"/>
        </dependency>
      </dependencies>
    </task>
  </taskgroup>
</pipeline>
'''
                }
            }
        ]
    }
}

snapshots['APITestCase::test_pipelines_modules_all_fields 1'] = {
    'pipelinesModulesList': {
        'edges': [
            {
                'node': {
                    'module': {
                        'moduleId': 461
                    },
                    'moduleId': 461,
                    'pipeline': {
                        'pipelineId': 176
                    },
                    'pipelineId': 176,
                    'xmlConfig': None
                }
            },
            {
                'node': {
                    'module': {
                        'moduleId': 501
                    },
                    'moduleId': 501,
                    'pipeline': {
                        'pipelineId': 176
                    },
                    'pipelineId': 176,
                    'xmlConfig': '''<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="/static/xml/mkform.xsl"?>
<config version="001" module="sky_partitioner">
  <section id="Sky partitioner">
    <subsection id="Partition setup">
      <scalar default="healpix" type="string" name="Partition method" id="partition_method">
        <values>
          <value value="healpix">Healpix</value>
          <value value="des_tiles">DES tiles</value>
        </values>
      </scalar>
    </subsection>
    <subsection id="Healpix setup">
      <scalar default="32" type="int" name="Healpix nside" id="healpix_nside">
        <values>
          <!--value>1</value><value>2</value-->
          <value>4</value>
          <value>8</value>
          <value>16</value>
          <value>32</value>
          <value>64</value>
          <value>128</value>
          <value>256</value>
          <value>512</value>
          <value>1024</value>
        </values>
      </scalar>
      <scalar default="true" type="string" name="Optimize Healpix nside reduction grouping sub-pixels of the same super-pixel in the same job" id="healpix_group_nside_reduction_by_job">
        <values>
          <value value="true">Yes</value>
          <value value="false">No</value>
        </values>
      </scalar>
    </subsection>
    <subsection id="DES tiles setup">
      <scalar default="1" type="int" name="Number of DES Tiles per Job" id="tiles_per_job">
        <values>
          <value>1</value>
          <value>2</value>
          <value>4</value>
          <value>8</value>
          <value>12</value>
          <value>24</value>
          <value>32</value>
          <value>48</value>
          <value>64</value>
          <value>128</value>
          <value>256</value>
          <value>512</value>
          <value>1024</value>
        </values>
      </scalar>
    </subsection>
  </section>
</config>
'''
                }
            },
            {
                'node': {
                    'module': {
                        'moduleId': 502
                    },
                    'moduleId': 502,
                    'pipeline': {
                        'pipelineId': 176
                    },
                    'pipelineId': 176,
                    'xmlConfig': '''<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="/static/xml/mkform.xsl"?>
<config version="001" module="partition_retriever">
  <section id="Setup">
    <subsection id="Split Internally">
      <scalar default="True" type="boolean" name="Split data into the exact amount of available processors?" id="split_internally">
        <values>
          <value value="True">Yes</value>
          <value value="False">No</value>
        </values>
      </scalar>
    </subsection>
  </section>
  <section id="Columns">
    <subsection id="Astrometry">
      <checkbox default="checked" type="column" name="ra" id="ra">
        <values>
          <value>RA</value>
        </values>
      </checkbox>
      <checkbox default="checked" type="column" name="dec" id="dec">
        <values>
          <value>DEC</value>
        </values>
      </checkbox>
      <checkbox default="checked" type="column" name="ebv" id="ebv">
        <values>
          <value>EBV</value>
        </values>
      </checkbox>
    </subsection>
    <subsection id="Base">
      <checkbox default="checked" type="column" name="coadd_objects_id" id="coadd_objects_id">
        <values>
          <value>COADD_OBJECTS_ID</value>
        </values>
      </checkbox>
    </subsection>
    <subsection id="Flux">
      <checkbox default="unchecked" type="column" name="flux_aper_3_[grizyu]" id="flux_aper_3_[grizyu]">
        <values>
          <value>FLUX_APER_3_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="flux_aper_4_[grizyu]" id="flux_aper_4_[grizyu]">
        <values>
          <value>FLUX_APER_4_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="fluxerr_aper_3_[grizyu]" id="fluxerr_aper_3_[grizyu]">
        <values>
          <value>FLUXERR_APER_3_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="fluxerr_aper_4_[grizyu]" id="fluxerr_aper_4_[grizyu]">
        <values>
          <value>FLUXERR_APER_4_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="flux_auto_[grizyu]" id="flux_auto_[grizyu]">
        <values>
          <value>FLUX_AUTO_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="fluxerr_auto_[grizyu]" id="fluxerr_auto_[grizyu]">
        <values>
          <value>FLUXERR_AUTO_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="flux_model_[grizyu]" id="flux_model_[grizyu]">
        <values>
          <value>FLUX_MODEL_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="fluxerr_model_[grizyu]" id="fluxerr_model_[grizyu]">
        <values>
          <value>FLUXERR_MODEL_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="flux_detmodel_[grizyu]" id="flux_detmodel_[grizyu]">
        <values>
          <value>FLUX_DETMODEL_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="fluxerr_detmodel_[grizyu]" id="fluxerr_detmodel_[grizyu]">
        <values>
          <value>FLUXERR_DETMODEL_[GRIZYU]</value>
        </values>
      </checkbox>
    </subsection>
    <subsection id="Magnitude">
      <checkbox default="checked" type="column" name="mag_auto_[grizyu]" id="mag_auto_[grizyu]">
        <values>
          <value>MAG_AUTO_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="mag_aper_3_[grizyu]" id="mag_aper_3_[grizyu]">
        <values>
          <value>MAG_APER_3_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="mag_aper_4_[grizyu]" id="mag_aper_4_[grizyu]">
        <values>
          <value>MAG_APER_4_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="magerr_aper_3_[grizyu]" id="magerr_aper_3_[grizyu]">
        <values>
          <value>MAGERR_APER_3_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="mag_aper_4_[grizyu]" id="mag_aper_4_[grizyu]">
        <values>
          <value>MAGERR_APER_4_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="checked" type="column" name="magerr_auto_[grizyu]" id="magerr_auto_[grizyu]">
        <values>
          <value>MAGERR_AUTO_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="mag_model_[grizyu]" id="mag_model_[grizyu]">
        <values>
          <value>MAG_MODEL_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="magerr_model_[grizyu]" id="magerr_model_[grizyu]">
        <values>
          <value>MAGERR_MODEL_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="checked" type="column" name="mag_detmodel_[grizyu]" id="mag_detmodel_[grizyu]">
        <values>
          <value>MAG_DETMODEL_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="magerr_detmodel_[grizyu]" id="magerr_detmodel_[grizyu]">
        <values>
          <value>MAGERR_DETMODEL_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="mu_max_[grizyu]" id="mu_max_[grizyu]">
        <values>
          <value>MU_MAX_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="mu_max_model_[grizyu]" id="mu_max_model_[grizyu]">
        <values>
          <value>MU_MAX_MODEL_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="mu_mean_model_[grizyu]" id="mu_mean_model_[grizyu]">
        <values>
          <value>MU_MEAN_MODEL_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="mu_threshold" id="mu_threshold">
        <values>
          <value>MU_THRESHOLD</value>
        </values>
      </checkbox>
      <checkbox default="checked" type="column" name="mu_eff_model_[grizyu]" id="mu_eff_model_[grizyu]">
        <values>
          <value>MU_EFF_MODEL_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="wavgcalib_mag_psf_[grizyu]" id="wavgcalib_mag_psf_[grizyu]">
        <values>
          <value>WAVGCALIB_MAG_PSF_[GRIZYU]</value>
        </values>
      </checkbox>
    </subsection>
    <subsection id="Model">
      <checkbox default="checked" type="column" name="niter_model_[grizyu]" id="niter_model_[grizyu]">
        <values>
          <value>NITER_MODEL_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="niter_psf_[grizyu]" id="niter_psf_[grizyu]">
        <values>
          <value>NITER_PSF_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="chi2_psf_[grizyu]" id="chi2_psf_[grizyu]">
        <values>
          <value>CHI2_PSF_[GRIZYU]</value>
        </values>
      </checkbox>
    </subsection>
    <subsection id="Quality">
      <checkbox default="checked" type="column" name="flags_[grizyu]" id="flags_[grizyu]">
        <values>
          <value>FLAGS_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="flags_model_[grizyu]" id="flags_model_[grizyu]">
        <values>
          <value>FLAGS_MODEL_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="flags_detmodel_[grizyu]" id="flags_detmodel_[grizyu]">
        <values>
          <value>FLAGS_DETMODEL_[GRIZYU]</value>
        </values>
      </checkbox>
    </subsection>
    <subsection id="Shape">
      <checkbox default="checked" type="column" name="spread_model_[grizyu]" id="spread_model_[grizyu]">
        <values>
          <value>SPREAD_MODEL_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="checked" type="column" name="spreaderr_model_[grizyu]" id="spreaderr_model_[grizyu]">
        <values>
          <value>SPREADERR_MODEL_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="checked" type="column" name="class_star_[grizyu]" id="class_star_[grizyu]">
        <values>
          <value>CLASS_STAR_[GRIZYU]</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="extended_class_mash_mof" id="extended_class_mash_mof">
        <values>
          <value>EXTENDED_CLASS_MASH_MOF</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="extended_class_mash_sof" id="extended_class_mash_sof">
        <values>
          <value>EXTENDED_CLASS_MASH_SOF</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="extended_class_mof" id="extended_class_mof">
        <values>
          <value>EXTENDED_CLASS_MOF</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="extended_class_sof" id="extended_class_sof">
        <values>
          <value>EXTENDED_CLASS_SOF</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="extended_class_wavg" id="extended_class_wavg">
        <values>
          <value>EXTENDED_CLASS_WAVG</value>
        </values>
      </checkbox>
      <checkbox default="unchecked" type="column" name="extended_class_coadd" id="extended_class_coadd">
        <values>
          <value>EXTENDED_CLASS_COADD</value>
        </values>
      </checkbox>
    </subsection>
  </section>
</config>
'''
                }
            }
        ]
    }
}

snapshots['APITestCase::test_processes_all_fields 1'] = {
    'processesList': {
        'edges': [
            {
                'node': {
                    'comments': None,
                    'configId': None,
                    'endIngestion': '2015-11-03T20:27:40',
                    'endTime': '2015-11-03T20:27:40',
                    'expirationTime': '2015-11-06T20:27:40',
                    'fields': {
                        'edges': [
                            {
                                'node': {
                                    'fieldId': 40
                                }
                            }
                        ]
                    },
                    'flagPublished': True,
                    'flagRemoved': False,
                    'idSite': '1',
                    'inputs': {
                        'edges': [
                        ]
                    },
                    'instance': 'testing',
                    'name': 'Install Catalogs',
                    'namespace': 'archive',
                    'processComments': {
                        'edges': [
                            {
                                'node': {
                                    'processId': 10021032
                                }
                            }
                        ]
                    },
                    'processDir': '/57/23/000010021032',
                    'processId': 10021032,
                    'processStatus': {
                        'processStatusId': 1
                    },
                    'products': {
                        'edges': [
                            {
                                'node': {
                                    'productId': 291773
                                }
                            }
                        ]
                    },
                    'publishedDate': '2016-03-25T11:54:18.502830',
                    'pypeInput': '''<?xml version="1.0" encoding="UTF-8"?>
<pipe>
  <summary>
    <field name="Field">Y1A1_COADD_STRIPE82</field>
    <provenance release_tag="Y1A1_COADD" display_name="v1.6" name="Data Release">v1.6(Y1A1_COADD)</provenance>
  </summary>
  <comment>&amp;lt;![CDATA[Running InstallCatalog without DownloadRequest over Y1A1 S82 to register products in the new database model]]&amp;gt;</comment>
</pipe>
''',
                    'readme': None,
                    'savedProcesses': {
                        'processId': 10021032
                    },
                    'session': {
                        'sessionId': '200861'
                    },
                    'sessionId': 200861,
                    'size': None,
                    'startIngestion': '2015-11-03T20:21:25',
                    'startTime': '2015-11-03T15:01:01',
                    'statusId': 1,
                    'xmlBeforeRun': None,
                    'xmlConfig': '''<?xml version="1.0" encoding="UTF-8"?>
<job name="Install Catalogs" pipeline_id="185" userId="374" session_id="200861" scratch_dir="/mnt/scratch/users/testing/master_des/000010021032/" publish_process="False" save_process="False">
  <components>
    <component display_name="Install" flow="1to1" id="install_catalogs" productLog="False">
      <module hdfslocator="False" multithreaded="False">install_catalogs</module>
      <input>
        <file mimetype="text/xml" type="" value="pype_input.xml" class="pype_input" source="scienceportal" optional="" id=""/>
      </input>
      <config>
        <scalar type="string" id="force_overwrite" value="No"/>
      </config>
    </component>
  </components>
</job>
'''
                }
            },
            {
                'node': {
                    'comments': None,
                    'configId': None,
                    'endIngestion': '2016-08-30T14:30:06',
                    'endTime': '2016-08-30T14:30:11',
                    'expirationTime': '2016-09-06T14:30:11',
                    'fields': {
                        'edges': [
                            {
                                'node': {
                                    'fieldId': 47
                                }
                            }
                        ]
                    },
                    'flagPublished': True,
                    'flagRemoved': False,
                    'idSite': '1',
                    'inputs': {
                        'edges': [
                        ]
                    },
                    'instance': 'testing',
                    'name': 'Install Catalogs',
                    'namespace': 'archive',
                    'processComments': {
                        'edges': [
                            {
                                'node': {
                                    'processId': 10024396
                                }
                            }
                        ]
                    },
                    'processDir': '/5b/37/000010024396',
                    'processId': 10024396,
                    'processStatus': {
                        'processStatusId': 1
                    },
                    'products': {
                        'edges': [
                            {
                                'node': {
                                    'productId': 291394
                                }
                            }
                        ]
                    },
                    'publishedDate': '2016-08-30T14:33:17.495773',
                    'pypeInput': '''<?xml version="1.0" encoding="UTF-8"?>
<pype>
  <comment>---</comment>
  <summary>
    <field display_name="COSMOS D04" name="Field">Y1A1_COADD_COSMOS_D04</field>
    <provenance release_tag="Y1A1_COADD" display_name="Y1A1" name="Data Release">v1.6(Y1A1_COADD)</provenance>
    <stage>Data Installation</stage>
    <type name="Number of objects">313380</type>
    <type name="Number of files">8</type>
  </summary>
</pype>
''',
                    'readme': None,
                    'savedProcesses': None,
                    'session': {
                        'sessionId': '200861'
                    },
                    'sessionId': 200861,
                    'size': 104,
                    'startIngestion': '2016-08-30T14:30:06',
                    'startTime': '2016-08-30T14:29:48',
                    'statusId': 1,
                    'xmlBeforeRun': None,
                    'xmlConfig': '''<?xml version="1.0" encoding="UTF-8"?>
<job name="Install Catalogs" pipeline_id="185" userId="133" session_id="200861" scratch_dir="/mnt/scratch/users/testing/master_des/000010024396" publish_process="False" save_process="False">
  <components>
    <component display_name="Install" flow="1to1" id="install_catalogs" productLog="False">
      <module hdfslocator="False" multithreaded="False" name="Catalog Installation">install_catalogs</module>
      <input>
        <file mimetype="text/xml" optional="" value="pype_input.xml" class="pype_input" source="scienceportal" type="" id=""/>
      </input>
      <config>
        <section id="Install Catalogs">
          <subsection id="Basic setup">
            <scalar id="force_overwrite" type="string" name="Force overwrite" value="No" description=""/>
          </subsection>
        </section>
      </config>
    </component>
  </components>
</job>
'''
                }
            },
            {
                'node': {
                    'comments': None,
                    'configId': None,
                    'endIngestion': '2018-06-05T20:32:16',
                    'endTime': '2018-06-05T20:32:19',
                    'expirationTime': '2018-06-12T20:32:19',
                    'fields': {
                        'edges': [
                            {
                                'node': {
                                    'fieldId': 40
                                }
                            }
                        ]
                    },
                    'flagPublished': False,
                    'flagRemoved': False,
                    'idSite': '1',
                    'inputs': {
                        'edges': [
                            {
                                'node': {
                                    'productId': 291773
                                }
                            }
                        ]
                    },
                    'instance': 'testing',
                    'name': 'WAZP',
                    'namespace': 'archive',
                    'processComments': {
                        'edges': [
                            {
                                'node': {
                                    'processId': 10031073
                                }
                            }
                        ]
                    },
                    'processDir': '/e2/66/000010031073',
                    'processId': 10031073,
                    'processStatus': {
                        'processStatusId': 1
                    },
                    'products': {
                        'edges': [
                            {
                                'node': {
                                    'productId': 308613
                                }
                            },
                            {
                                'node': {
                                    'productId': 308614
                                }
                            }
                        ]
                    },
                    'publishedDate': None,
                    'pypeInput': '''<?xml version="1.0" encoding="UTF-8"?>
<pype>
  <comment>validation run</comment>
  <input>
    <product process_path="/process/testing/92/4c/000010028241" display_name="Cluster Catalog" product_id="306732" type_name="Value-Added Catalogs" catalog_name="cluster catalog " class="vac_cluster" process_id="10028241" table="photo_z_10028241" type="value_added_catalogs" product_name="Cluster Catalog 121" schema="vac_cluster"/>
    <parents>
      <parent process_path="/process/testing/c9/e2/000010018969" process_id="10018969" display_name="Upload" stage="Utilities"/>
      <parent process_path="/process/testing/f7/7e/000010019503" process_id="10019503" display_name="Upload" stage="Utilities"/>
      <parent process_path="/process/testing/48/46/000010021024" process_id="10021024" display_name="Upload" stage="Utilities"/>
      <parent process_path="/process/testing/57/23/000010021032" process_id="10021032" display_name="Install Catalogs" stage="Data Installation"/>
      <parent process_path="/process/testing/32/80/000010021144" process_id="10021144" display_name="Upload" stage="Utilities"/>
      <parent process_path="/process/testing/09/55/000010022127" process_id="10022127" display_name="Upload" stage="Utilities"/>
      <parent process_path="/process/testing/2c/47/000010022543" process_id="10022543" display_name="Upload" stage="Utilities"/>
      <parent process_path="/process/testing/93/3a/000010022633" process_id="10022633" display_name="Upload" stage="Utilities"/>
      <parent process_path="/process/testing/bf/de/000010022644" process_id="10022644" display_name="Zeropoint Correction" stage="Data Installation"/>
      <parent process_path="/process/testing/c1/80/000010022779" process_id="10022779" display_name="Upload" stage="Utilities"/>
      <parent process_path="/process/testing/9d/23/000010023395" process_id="10023395" display_name="Zeropoint Correction" stage="Data Installation"/>
      <parent process_path="/process/testing/5b/37/000010024396" process_id="10024396" display_name="Install Catalogs" stage="Data Installation"/>
      <parent process_path="/process/testing/9d/74/000010028092" process_id="10028092" display_name="SG Separation" stage="Data Preparation"/>
      <parent process_path="/process/testing/e1/cd/000010028227" process_id="10028227" display_name="SG Separation" stage="Data Preparation"/>
      <parent process_path="/process/testing/e1/cd/000010028229" process_id="10028229" display_name="Spectroscopic Sample" stage="Data Preparation"/>
      <parent process_path="/process/testing/e1/cd/000010028230" process_id="10028230" display_name="Training Set Maker" stage="Data Preparation"/>
      <parent process_path="/process/testing/e1/cd/000010028231" process_id="10028231" display_name="Photo-z Training" stage="Data Preparation"/>
      <parent process_path="/process/testing/92/4c/000010028239" process_id="10028239" display_name="Photo-z Compute" stage="Data Preparation"/>
      <parent process_path="/process/testing/92/4c/000010028241" process_id="10028241" display_name="Cluster" stage="Science-Ready Catalogs"/>
    </parents>
  </input>
  <summary>
    <field display_name="STRIPE82" name="Field">Y1A1_COADD_STRIPE82</field>
    <provenance release_tag="Y1A1_COADD" display_name="Y1A1" name="Data Release">v1.6(Y1A1_COADD)</provenance>
    <stage>Science Analysis</stage>
    <type name="ZP correction">SFD98</type>
    <type name="Extinction map">None</type>
    <type name="ZP correction">SFD98</type>
    <type name="Extinction map">None</type>
    <type name="Footprint area:">146.11 sq deg</type>
    <type name="Mean density:">3.58 objects/(sq arcmin)</type>
    <type name="Photo-z">DNF</type>
    <type name="S/G Classification">Y1 Modest v3</type>
  </summary>
</pype>
''',
                    'readme': None,
                    'savedProcesses': None,
                    'session': {
                        'sessionId': '200861'
                    },
                    'sessionId': 200861,
                    'size': 8271408,
                    'startIngestion': '2018-06-05T20:32:16',
                    'startTime': '2018-06-05T20:20:53',
                    'statusId': 1,
                    'xmlBeforeRun': None,
                    'xmlConfig': '''<?xml version="1.0" encoding="UTF-8"?>
<job name="WAZP" pipeline_id="214" userId="345" session_id="200861" scratch_dir="/mnt/scratch/users/testing/master_des/000010031073" publish_process="False" save_process="False">
  <components>
    <component display_name="Slicing" flow="1to1" id="wazp_slice_zmag" productLog="False">
      <module hdfslocator="False" multithreaded="False" name="Slicing">wazp_slice_zmag</module>
      <input>
        <file mimetype="text/xml" optional="" value="pype_input.xml" class="pype_input" source="scienceportal" type="" id=""/>
      </input>
      <config>
        <section id="WAZP Configuration">
          <subsection id="Spatial tiling">
            <scalar id="SPLIT_DATA" type="string" name="Data split" value="YES" description=""/>
            <scalar id="AREA" type="string" name="Total area for detection before trim" value="20." description=""/>
            <scalar id="OVERLAP" type="string" name="Overlap" value="0.8" description=""/>
          </subsection>
          <subsection id="Zphot slicing">
            <scalar id="SIGMA_DZ_MODE" type="string" name="SIGMA DZ MODE" value="VAR" description=""/>
            <scalar id="SIGMA_DZ" type="string" name="SIGMA DZ" value="0.0" description=""/>
          </subsection>
          <subsection id="Cluster detection parameters">
            <scalar id="DMAG" type="string" name="DMAG (m_faint - m_star for Richness)" value="2." description=""/>
            <scalar id="DMAG_BRIGHT" type="string" name="DMAG_BRIGHT (m_star - m_bright)" value="3." description=""/>
            <scalar id="DMAG_DET" type="string" name="DMAG_DET (m_faint - m_star for detection)" value="2." description=""/>
            <scalar id="SNR_LIM" type="string" name="S/N detection" value="2.0" description=""/>
            <scalar id="SNR_MR" type="string" name="S/N MR filter" value="3.0" description=""/>
            <scalar name="Contrast limit for NGAL/Radius" value="2." hidden="hidden" type="string" id="CONTRAST_LIM" description=""/>
            <scalar id="DETECT_MODE" type="string" name="DETECT mode" value="L" description=""/>
            <scalar id="BKG_MODE" type="string" name="BKG mode" value="L" description=""/>
            <scalar name="BKG max number of tiles" value="30" hidden="hidden" type="string" id="BKG_NTILES_MAX" description=""/>
            <scalar name="CL SIZE MIN" value="0.35" hidden="hidden" type="string" id="CL_SIZE_MIN" description=""/>
            <scalar name="CL SIZE MAX" value="1.5" hidden="hidden" type="string" id="CL_SIZE_MAX" description=""/>
            <scalar name="Resolution" value="16" hidden="hidden" type="string" id="RESOLUTION" description=""/>
            <scalar name="Resolution Z" value="0.002" hidden="hidden" type="string" id="RESOLUTION_Z" description=""/>
            <scalar name="TMP RUN" value="NO" hidden="hidden" type="string" id="tmp_RUN" description=""/>
            <scalar name="SURVEY_NAME" value="PORTAL" hidden="hidden" type="string" id="SURVEY_NAME" description=""/>
            <scalar name="PATH_DATA" value="" hidden="hidden" type="string" id="PATH_DATA" description=""/>
            <scalar name="Data type" value="REAL" hidden="hidden" type="string" id="DATA_TYPE" description=""/>
            <scalar id="FILTER" type="string" name="Filter" value="i" description=""/>
            <scalar id="MAGLIM" type="string" name="Magnitude limit" value="22." description=""/>
          </subsection>
          <subsection id="Cluster radius / Richness / Ranking">
            <scalar id="KEY_RANK" type="string" name="Key rank: to rank the cluster list" value="SNR" description=""/>
          </subsection>
          <subsection id="Execution mode">
            <scalar id="IVERBOSE" type="string" name="IVERBOSE" value="1" description=""/>
          </subsection>
        </section>
      </config>
    </component>
    <component display_name="Split Area" flow="1toN" id="wazp_split_area" productLog="False">
      <module hdfslocator="False" multithreaded="False" name="Split Area">wazp_split_area</module>
      <input>
        <file mimetype="text/xml" optional="" value="pype_input.xml" class="pype_input" source="scienceportal" type="" id=""/>
        <file mimetype="text/plain" optional="True" value="" id="" source="wazp_slice_zmag" type="" class="wazp_config"/>
      </input>
      <config/>
    </component>
    <component display_name="Visibility Maps" flow="1to1" id="wazp_visibility_maps" productLog="False">
      <module hdfslocator="False" multithreaded="False" name="Visibility Maps">wazp_visibility_maps</module>
      <input>
        <file mimetype="text/xml" optional="" value="pype_input.xml" class="pype_input" source="scienceportal" type="" id=""/>
        <file mimetype="text/plain" optional="True" value="" id="" source="wazp_slice_zmag" type="" class="calib_zmag_slice"/>
        <file mimetype="text/plain" optional="True" value="" id="" source="wazp_slice_zmag" type="" class="wazp_config"/>
        <file mimetype="text/plain" optional="True" value="" id="" source="wazp_split_area" type="" class="tile_vertices"/>
        <file mimetype="text/plain" optional="True" value="" id="" source="wazp_split_area" type="" class="footprint_txt"/>
      </input>
      <config/>
    </component>
    <component display_name="Background modelling per tile" flow="1to1" id="wazp_bkg_model" productLog="False">
      <module hdfslocator="False" multithreaded="False" name="Background modelling per tile">wazp_bkg_model</module>
      <input>
        <file mimetype="text/plain" optional="True" value="" id="" source="wazp_slice_zmag" type="" class="calib_zmag_slice"/>
        <file mimetype="text/plain" optional="True" value="" id="" source="wazp_slice_zmag" type="" class="wazp_config"/>
        <file mimetype="text/plain" optional="True" value="" id="" source="wazp_split_area" type="" class="tile_vertices"/>
        <file mimetype="application/fits-table" optional="True" value="" id="" source="wazp_visibility_maps" type="" class="visibility_map_trim"/>
        <file mimetype="application/fits-table" optional="True" value="" id="" source="wazp_visibility_maps" type="" class="vac_cluster"/>
      </input>
      <config/>
    </component>
    <component display_name="Background concatenation" flow="Nto1" id="wazp_bkg_concat" productLog="False">
      <module hdfslocator="False" multithreaded="False" name="Background concatenation">wazp_bkg_concat</module>
      <input>
        <file mimetype="text/plain" optional="True" value="" id="" source="wazp_slice_zmag" type="" class="calib_zmag_slice"/>
        <file mimetype="text/plain" optional="True" value="" id="" source="wazp_slice_zmag" type="" class="wazp_config"/>
        <file mimetype="text/plain" type="" value="" optiona="True" source="wazp_split_area" id="" optional="" class="tiles_list"/>
        <file mimetype="application/fits-table" optional="True" value="" id="" source="wazp_visibility_maps" type="" class="visibility_map_trim"/>
        <file mimetype="application/x-tar" optional="True" value="" id="" source="wazp_bkg_model" type="" class="bkg_model"/>
      </input>
      <config/>
    </component>
    <component transfer="False" flow="1toN" display_name="WAZP split per tile" id="wazp_pre_tile" productLog="False">
      <module hdfslocator="False" multithreaded="False" name="WAZP split per tile">wazp_pre_tile</module>
      <input>
        <file mimetype="text/plain" optional="True" value="" id="" source="wazp_slice_zmag" type="" class="calib_zmag_slice"/>
        <file mimetype="text/plain" optional="True" value="" id="" source="wazp_slice_zmag" type="" class="wazp_config"/>
        <file mimetype="text/plain" optional="True" value="" id="" source="wazp_split_area" type="" class="tile_vertices"/>
        <file mimetype="application/fits-table" optional="True" value="" id="" source="wazp_visibility_maps" type="" class="visibility_maps"/>
        <file mimetype="application/fits-table" optional="True" value="" id="" source="wazp_visibility_maps" type="" class="vac_cluster"/>
        <file mimetype="text/plain" optional="True" value="" id="" source="wazp_bkg_concat" type="" class="bkg_model"/>
        <file mimetype="text/plain" optional="True" value="" id="" source="wazp_bkg_concat" type="" class="bkg_model_mag"/>
      </input>
      <config/>
    </component>
    <component display_name="Cluster detection per tile" flow="1to1" id="wazp_tile" productLog="False">
      <module hdfslocator="False" multithreaded="False" name="Cluster detection per tile">wazp_tile</module>
      <input>
        <file mimetype="text/plain" optional="True" value="" id="" source="wazp_slice_zmag" type="" class="calib_zmag_slice"/>
        <file mimetype="text/plain" optional="True" value="" id="" source="wazp_slice_zmag" type="" class="wazp_config"/>
        <file mimetype="text/plain" optional="True" value="" id="" source="wazp_split_area" type="" class="tile_vertices"/>
        <config mimetype="" type="string" value="" class="" source="wazp_split_area" optional="True" id="tile_max_area"/>
        <file mimetype="application/fits-table" optional="True" value="" id="" source="wazp_visibility_maps" type="" class="visibility_maps"/>
        <file mimetype="application/fits-table" optional="True" value="" id="" source="wazp_visibility_maps" type="" class="vac_cluster"/>
        <file mimetype="text/plain" optional="True" value="" id="" source="wazp_bkg_concat" type="" class="bkg_model"/>
        <file mimetype="text/plain" optional="True" value="" id="" source="wazp_bkg_concat" type="" class="bkg_model_mag"/>
      </input>
      <config/>
    </component>
    <component display_name="Clusters concatenation" flow="Nto1" id="wazp_concatenate" productLog="False">
      <module hdfslocator="False" multithreaded="True" name="Clusters concatenation">wazp_concatenate</module>
      <input>
        <file mimetype="text/xml" optional="" value="pype_input.xml" class="pype_input" source="scienceportal" type="" id=""/>
        <file mimetype="text/plain" optional="True" value="" id="" source="wazp_slice_zmag" type="" class="wazp_config"/>
        <config mimetype="" type="string" value="" class="" source="wazp_slice_zmag" optional="True" id="vac_area"/>
        <file mimetype="text/plain" optional="True" value="" id="" source="wazp_split_area" type="" class="tiles_list"/>
        <file mimetype="application/fits-table" optional="True" value="" id="" source="wazp_tile" type="" class="cluster_list"/>
        <file mimetype="application/fits-table" optional="True" value="" id="" source="wazp_tile" type="" class="member_list"/>
        <file mimetype="text/plain" optional="True" value="" id="" source="wazp_tile" type="" class="tile_coords"/>
        <file mimetype="image/png" optional="True" value="" id="" source="wazp_tile" type="" class="histo_zp"/>
        <file mimetype="image/png" optional="True" value="" id="" source="wazp_tile" type="" class="zph_mag"/>
      </input>
      <config/>
    </component>
  </components>
</job>
'''
                }
            }
        ]
    }
}

snapshots['APITestCase::test_product_class_all_fields 1'] = {
    'productClassList': {
        'edges': [
            {
                'node': {
                    'classId': 94,
                    'className': 'bcc_simulation',
                    'displayName': 'BCC',
                    'isSystem': None,
                    'productType': {
                        'typeId': 3
                    },
                    'typeId': 3
                }
            },
            {
                'node': {
                    'classId': 95,
                    'className': 'mice_simulation',
                    'displayName': 'Mice',
                    'isSystem': None,
                    'productType': {
                        'typeId': 3
                    },
                    'typeId': 3
                }
            },
            {
                'node': {
                    'classId': 96,
                    'className': 'addstar_simulation',
                    'displayName': 'Addstar',
                    'isSystem': None,
                    'productType': {
                        'typeId': 3
                    },
                    'typeId': 3
                }
            },
            {
                'node': {
                    'classId': 101,
                    'className': 'astrometry_outliers',
                    'displayName': 'Astrometry Outliers',
                    'isSystem': None,
                    'productType': {
                        'typeId': 1
                    },
                    'typeId': 1
                }
            },
            {
                'node': {
                    'classId': 2,
                    'className': 'galaxy_clusters',
                    'displayName': 'Galaxy Clusters',
                    'isSystem': True,
                    'productType': {
                        'typeId': 1
                    },
                    'typeId': 1
                }
            }
        ]
    }
}

snapshots['APITestCase::test_product_type_all_fields 1'] = {
    'productTypeList': {
        'edges': [
            {
                'node': {
                    'displayName': 'Targets',
                    'typeId': 1,
                    'typeName': 'targets'
                }
            },
            {
                'node': {
                    'displayName': 'Simulations',
                    'typeId': 3,
                    'typeName': 'simulations'
                }
            },
            {
                'node': {
                    'displayName': 'Value-Added Catalogs',
                    'typeId': 2,
                    'typeName': 'value_added_catalogs'
                }
            },
            {
                'node': {
                    'displayName': 'Objects Catalog',
                    'typeId': 4,
                    'typeName': 'objects_catalog'
                }
            }
        ]
    }
}

snapshots['APITestCase::test_products_all_fields 1'] = {
    'productsList': {
        'edges': [
            {
                'node': {
                    'Class': {
                        'classId': 11
                    },
                    'classId': 11,
                    'displayName': 'Coadd Objects ',
                    'file': None,
                    'fileId': None,
                    'flagRemoved': False,
                    'job': {
                        'jobId': 914484
                    },
                    'jobId': 914484,
                    'process': {
                        'processId': 10024396
                    },
                    'processId': 10024396,
                    'productId': 291394,
                    'selectedName': None,
                    'table': {
                        'tableId': 46
                    },
                    'tableId': 46,
                    'version': None
                }
            },
            {
                'node': {
                    'Class': {
                        'classId': 11
                    },
                    'classId': 11,
                    'displayName': 'Coadd Objects ',
                    'file': None,
                    'fileId': None,
                    'flagRemoved': False,
                    'job': {
                        'jobId': 872322
                    },
                    'jobId': 872322,
                    'process': {
                        'processId': 10021032
                    },
                    'processId': 10021032,
                    'productId': 291773,
                    'selectedName': None,
                    'table': {
                        'tableId': 399
                    },
                    'tableId': 399,
                    'version': None
                }
            },
            {
                'node': {
                    'Class': {
                        'classId': 2
                    },
                    'classId': 2,
                    'displayName': 'Galaxy Clusters 58',
                    'file': {
                        'fileId': 476683
                    },
                    'fileId': 476683,
                    'flagRemoved': False,
                    'job': {
                        'jobId': 965402
                    },
                    'jobId': 965402,
                    'process': {
                        'processId': 10031073
                    },
                    'processId': 10031073,
                    'productId': 308613,
                    'selectedName': None,
                    'table': None,
                    'tableId': None,
                    'version': 58
                }
            }
        ]
    }
}

snapshots['APITestCase::test_release_tag_all_fields 1'] = {
    'releaseTagList': {
        'edges': [
            {
                'node': {
                    'description': 'A subset of Y1A1_COADD coadds in the Stripe82 region.',
                    'docUrl': 'https://deswiki.cosmology.illinois.edu/confluence/x/BgAi',
                    'fields': {
                        'edges': [
                            {
                                'node': {
                                    'fieldId': 47
                                }
                            },
                            {
                                'node': {
                                    'fieldId': 40
                                }
                            },
                            {
                                'node': {
                                    'fieldId': 64
                                }
                            }
                        ]
                    },
                    'name': 'Y1A1_COADD',
                    'releaseDate': '2014-10-10',
                    'releaseDisplayName': 'Y1A1',
                    'tagId': 24,
                    'version': 'v1.6'
                }
            }
        ]
    }
}

snapshots['APITestCase::test_search_and_sort 1'] = {
    'productClassList': {
        'edges': [
            {
                'node': {
                    'className': 'vac_bright_mask',
                    'displayName': 'Bad Regions Map',
                    'productType': {
                        'typeName': 'value_added_catalogs'
                    }
                }
            },
            {
                'node': {
                    'className': 'vac_cluster',
                    'displayName': 'Cluster Catalog',
                    'productType': {
                        'typeName': 'value_added_catalogs'
                    }
                }
            },
            {
                'node': {
                    'className': 'coadd_objects',
                    'displayName': 'Coadd Objects',
                    'productType': {
                        'typeName': 'objects_catalog'
                    }
                }
            }
        ]
    }
}

snapshots['APITestCase::test_search_nested_table 1'] = {
    'productClassList': {
        'edges': [
            {
                'node': {
                    'className': 'vac_generic',
                    'displayName': 'Generic',
                    'productType': {
                        'typeName': 'value_added_catalogs'
                    }
                }
            },
            {
                'node': {
                    'className': 'vac_cluster',
                    'displayName': 'Cluster Catalog',
                    'productType': {
                        'typeName': 'value_added_catalogs'
                    }
                }
            },
            {
                'node': {
                    'className': 'vac_ga',
                    'displayName': 'GA',
                    'productType': {
                        'typeName': 'value_added_catalogs'
                    }
                }
            }
        ]
    }
}

snapshots['APITestCase::test_search_same_table 1'] = {
    'productClassList': {
        'edges': [
            {
                'node': {
                    'className': 'bcc_simulation',
                    'displayName': 'BCC'
                }
            },
            {
                'node': {
                    'className': 'mice_simulation',
                    'displayName': 'Mice'
                }
            },
            {
                'node': {
                    'className': 'addstar_simulation',
                    'displayName': 'Addstar'
                }
            }
        ]
    }
}

snapshots['APITestCase::test_fields 1'] = {
    'fieldsList': {
        'edges': [
            {
                'node': {
                    'fieldId': 47,
                    'fieldName': 'Y1A1_COADD_COSMOS_D04',
                    'releaseTag': {
                        'name': 'Y1A1_COADD',
                        'tagId': 24
                    }
                }
            },
            {
                'node': {
                    'fieldId': 40,
                    'fieldName': 'Y1A1_COADD_STRIPE82',
                    'releaseTag': {
                        'name': 'Y1A1_COADD',
                        'tagId': 24
                    }
                }
            },
            {
                'node': {
                    'fieldId': 64,
                    'fieldName': 'Y3_GOLD',
                    'releaseTag': {
                        'name': 'Y1A1_COADD',
                        'tagId': 24
                    }
                }
            }
        ]
    }
}

snapshots['APITestCase::test_pipelines 1'] = {
    'pipelinesList': {
        'edges': [
            {
                'cursor': 'YXJyYXljb25uZWN0aW9uOjE=',
                'node': {
                    'displayName': 'Install Catalogs',
                    'group': {
                        'displayName': 'Hidden'
                    },
                    'name': 'install_catalogs',
                    'pipelineStage': {
                        'displayName': 'Data Installation'
                    },
                    'readme': None,
                    'user': {
                        'displayName': 'Test User'
                    },
                    'versionDate': '2016-04-06T10:16:48'
                }
            },
            {
                'cursor': 'YXJyYXljb25uZWN0aW9uOjI=',
                'node': {
                    'displayName': 'Cluster',
                    'group': {
                        'displayName': 'Science-Ready Catalogs'
                    },
                    'name': 'vac_cluster',
                    'pipelineStage': {
                        'displayName': 'Science-Ready Catalogs'
                    },
                    'readme': None,
                    'user': {
                        'displayName': 'Test User'
                    },
                    'versionDate': '2018-07-19T14:05:23'
                }
            },
            {
                'cursor': 'YXJyYXljb25uZWN0aW9uOjM=',
                'node': {
                    'displayName': 'Data Installation',
                    'group': {
                        'displayName': 'Hidden'
                    },
                    'name': 'data_installation',
                    'pipelineStage': {
                        'displayName': 'Data Installation'
                    },
                    'readme': None,
                    'user': {
                        'displayName': 'Test User'
                    },
                    'versionDate': '2016-04-06T10:15:48'
                }
            },
            {
                'cursor': 'YXJyYXljb25uZWN0aW9uOjQ=',
                'node': {
                    'displayName': 'Photo-z Compute',
                    'group': {
                        'displayName': 'Data Preparation'
                    },
                    'name': 'photoz_compute',
                    'pipelineStage': {
                        'displayName': 'Data Preparation'
                    },
                    'readme': 'https://docs.google.com/document/d/1yHUklXgtOz6rI9ERVJOhXHUdzez8jeVjFqUGNGUC0wA/edit?usp=sharing',
                    'user': {
                        'displayName': 'Test User'
                    },
                    'versionDate': '2018-09-06T15:43:41.062835'
                }
            }
        ]
    }
}

snapshots['APITestCase::test_pipelines_modules 1'] = {
    'pipelinesModulesList': {
        'edges': [
            {
                'cursor': 'YXJyYXljb25uZWN0aW9uOjM=',
                'node': {
                    'module': {
                        'displayName': 'DNF',
                        'name': 'dnf',
                        'user': {
                            'displayName': 'Test User'
                        },
                        'version': 'V03_03_14',
                        'versionDate': '2018-09-04T17:45:15.523132'
                    },
                    'pipeline': {
                        'displayName': 'Photo-z Compute'
                    }
                }
            },
            {
                'cursor': 'YXJyYXljb25uZWN0aW9uOjQ=',
                'node': {
                    'module': {
                        'displayName': 'ANNz',
                        'name': 'annz',
                        'user': {
                            'displayName': 'Test User'
                        },
                        'version': 'V02_08_10',
                        'versionDate': '2018-09-04T17:45:15.523132'
                    },
                    'pipeline': {
                        'displayName': 'Photo-z Compute'
                    }
                }
            },
            {
                'cursor': 'YXJyYXljb25uZWN0aW9uOjU=',
                'node': {
                    'module': {
                        'displayName': 'ANNz2',
                        'name': 'annz2',
                        'user': {
                            'displayName': 'Test User'
                        },
                        'version': 'V02_00_05',
                        'versionDate': '2018-09-04T17:45:15.523132'
                    },
                    'pipeline': {
                        'displayName': 'Photo-z Compute'
                    }
                }
            },
            {
                'cursor': 'YXJyYXljb25uZWN0aW9uOjY=',
                'node': {
                    'module': {
                        'displayName': 'BPZ',
                        'name': 'bpz',
                        'user': {
                            'displayName': 'Test User'
                        },
                        'version': 'V00_02_02',
                        'versionDate': '2018-09-04T17:45:15.523132'
                    },
                    'pipeline': {
                        'displayName': 'Photo-z Compute'
                    }
                }
            },
            {
                'cursor': 'YXJyYXljb25uZWN0aW9uOjc=',
                'node': {
                    'module': {
                        'displayName': 'MLZ',
                        'name': 'mlz',
                        'user': {
                            'displayName': 'Test User'
                        },
                        'version': 'V01_08_08',
                        'versionDate': '2018-09-04T17:45:15.523132'
                    },
                    'pipeline': {
                        'displayName': 'Photo-z Compute'
                    }
                }
            }
        ]
    }
}

snapshots['APITestCase::test_processes 1'] = {
    'processesList': {
        'edges': [
            {
                'cursor': 'YXJyYXljb25uZWN0aW9uOjA=',
                'node': {
                    'endTime': '2015-11-03T20:27:40',
                    'fields': {
                        'edges': [
                            {
                                'node': {
                                    'fieldName': 'Y1A1_COADD_STRIPE82',
                                    'releaseTag': {
                                        'releaseDisplayName': 'Y1A1'
                                    }
                                }
                            }
                        ]
                    },
                    'flagPublished': True,
                    'instance': 'testing',
                    'name': 'Install Catalogs',
                    'processId': 10021032,
                    'processStatus': {
                        'name': 'success'
                    },
                    'savedProcesses': {
                        'savedDate': '2015-11-03T20:27:40',
                        'savedDateEnd': '2015-11-03T21:43:41'
                    },
                    'session': {
                        'user': {
                            'displayName': 'Test User'
                        }
                    },
                    'startTime': '2015-11-03T15:01:01'
                }
            },
            {
                'cursor': 'YXJyYXljb25uZWN0aW9uOjE=',
                'node': {
                    'endTime': '2016-08-30T14:30:11',
                    'fields': {
                        'edges': [
                            {
                                'node': {
                                    'fieldName': 'Y1A1_COADD_COSMOS_D04',
                                    'releaseTag': {
                                        'releaseDisplayName': 'Y1A1'
                                    }
                                }
                            }
                        ]
                    },
                    'flagPublished': True,
                    'instance': 'testing',
                    'name': 'Install Catalogs',
                    'processId': 10024396,
                    'processStatus': {
                        'name': 'success'
                    },
                    'savedProcesses': None,
                    'session': {
                        'user': {
                            'displayName': 'Test User'
                        }
                    },
                    'startTime': '2016-08-30T14:29:48'
                }
            }
        ],
        'pageInfo': {
            'endCursor': 'YXJyYXljb25uZWN0aW9uOjE=',
            'startCursor': 'YXJyYXljb25uZWN0aW9uOjA='
        },
        'totalCount': 2
    }
}

snapshots['APITestCase::test_product_class 1'] = {
    'productClassList': {
        'edges': [
            {
                'cursor': 'YXJyYXljb25uZWN0aW9uOjM=',
                'node': {
                    'className': 'astrometry_outliers',
                    'displayName': 'Astrometry Outliers',
                    'productType': {
                        'displayName': 'Targets',
                        'typeName': 'targets'
                    }
                }
            },
            {
                'cursor': 'YXJyYXljb25uZWN0aW9uOjQ=',
                'node': {
                    'className': 'galaxy_clusters',
                    'displayName': 'Galaxy Clusters',
                    'productType': {
                        'displayName': 'Targets',
                        'typeName': 'targets'
                    }
                }
            },
            {
                'cursor': 'YXJyYXljb25uZWN0aW9uOjU=',
                'node': {
                    'className': 'stellar_systems',
                    'displayName': 'Stellar Systems',
                    'productType': {
                        'displayName': 'Targets',
                        'typeName': 'targets'
                    }
                }
            },
            {
                'cursor': 'YXJyYXljb25uZWN0aW9uOjY=',
                'node': {
                    'className': 'cluster_members',
                    'displayName': 'Cluster Members',
                    'productType': {
                        'displayName': 'Targets',
                        'typeName': 'targets'
                    }
                }
            },
            {
                'cursor': 'YXJyYXljb25uZWN0aW9uOjc=',
                'node': {
                    'className': 'vac_generic',
                    'displayName': 'Generic',
                    'productType': {
                        'displayName': 'Value-Added Catalogs',
                        'typeName': 'value_added_catalogs'
                    }
                }
            }
        ]
    }
}

snapshots['APITestCase::test_products 1'] = {
    'productsList': {
        'edges': [
            {
                'node': {
                    'displayName': 'Cluster Members 58',
                    'process': {
                        'processId': 10031073
                    },
                    'productId': 308614
                }
            },
            {
                'node': {
                    'displayName': 'Galaxy Clusters 58',
                    'process': {
                        'processId': 10031073
                    },
                    'productId': 308613
                }
            }
        ]
    }
}

snapshots['APITestCase::test_release_tag 1'] = {
    'releaseTagList': {
        'edges': [
            {
                'node': {
                    'description': 'A subset of Y1A1_COADD coadds in the Stripe82 region.',
                    'docUrl': 'https://deswiki.cosmology.illinois.edu/confluence/x/BgAi',
                    'fields': {
                        'edges': [
                            {
                                'node': {
                                    'status': True
                                }
                            },
                            {
                                'node': {
                                    'status': True
                                }
                            },
                            {
                                'node': {
                                    'status': True
                                }
                            }
                        ]
                    },
                    'name': 'Y1A1_COADD',
                    'releaseDate': '2014-10-10',
                    'releaseDisplayName': 'Y1A1',
                    'tagId': 24,
                    'version': 'v1.6'
                }
            }
        ]
    }
}

snapshots['APITestCase::test_release_tag_only_available_true 1'] = {
    'releaseTagList': {
        'edges': [
            {
                'node': {
                    'description': 'A subset of Y1A1_COADD coadds in the Stripe82 region.',
                    'docUrl': 'https://deswiki.cosmology.illinois.edu/confluence/x/BgAi',
                    'fields': {
                        'edges': [
                            {
                                'node': {
                                    'status': True
                                }
                            },
                            {
                                'node': {
                                    'status': True
                                }
                            },
                            {
                                'node': {
                                    'status': True
                                }
                            }
                        ]
                    },
                    'name': 'Y1A1_COADD',
                    'releaseDate': '2014-10-10',
                    'releaseDisplayName': 'Y1A1',
                    'tagId': 24,
                    'version': 'v1.6'
                }
            }
        ]
    }
}

snapshots['APITestCase::test_modules_pipelines 1'] = {
    'modulesList': {
        'edges': [
            {
                'node': {
                    'displayName': 'Catalog Installation',
                    'moduleId': 396,
                    'name': 'install_catalogs',
                    'pipelinesModules': {
                        'edges': [
                            {
                                'node': {
                                    'pipeline': {
                                        'displayName': 'Data Installation',
                                        'name': 'data_installation',
                                        'pipelineId': 174
                                    }
                                }
                            }
                        ]
                    },
                    'user': {
                        'displayName': 'Test User',
                        'userName': 'linea'
                    }
                }
            },
            {
                'node': {
                    'displayName': 'LePhare',
                    'moduleId': 255,
                    'name': 'lephare_new',
                    'pipelinesModules': {
                        'edges': [
                            {
                                'node': {
                                    'pipeline': {
                                        'displayName': 'Photo-z Compute',
                                        'name': 'photoz_compute',
                                        'pipelineId': 176
                                    }
                                }
                            }
                        ]
                    },
                    'user': {
                        'displayName': 'Test User',
                        'userName': 'linea'
                    }
                }
            },
            {
                'node': {
                    'displayName': 'Sky Partitioner',
                    'moduleId': 501,
                    'name': 'sky_partitioner',
                    'pipelinesModules': {
                        'edges': [
                            {
                                'node': {
                                    'pipeline': {
                                        'displayName': 'Photo-z Compute',
                                        'name': 'photoz_compute',
                                        'pipelineId': 176
                                    }
                                }
                            }
                        ]
                    },
                    'user': {
                        'displayName': 'Test User',
                        'userName': 'linea'
                    }
                }
            },
            {
                'node': {
                    'displayName': 'Partition Retreiver',
                    'moduleId': 502,
                    'name': 'partition_retriever',
                    'pipelinesModules': {
                        'edges': [
                            {
                                'node': {
                                    'pipeline': {
                                        'displayName': 'Photo-z Compute',
                                        'name': 'photoz_compute',
                                        'pipelineId': 176
                                    }
                                }
                            }
                        ]
                    },
                    'user': {
                        'displayName': 'Test User',
                        'userName': 'linea'
                    }
                }
            },
            {
                'node': {
                    'displayName': 'Clusters concatenation',
                    'moduleId': 491,
                    'name': 'wazp_concatenate',
                    'pipelinesModules': {
                        'edges': [
                            {
                                'node': {
                                    'pipeline': {
                                        'displayName': 'WAZP',
                                        'name': 'wazp_new',
                                        'pipelineId': 214
                                    }
                                }
                            }
                        ]
                    },
                    'user': {
                        'displayName': 'Test User',
                        'userName': 'linea'
                    }
                }
            }
        ]
    }
}

snapshots['APITestCase::test_pipelines_by_stage_id_and_tag_id_and_field_id 1'] = {
    'pipelinesByStageIdAndTagIdAndFieldId': {
        'edges': [
            {
                'node': {
                    'lastProcessEndTime': '2018-06-05T20:32:19',
                    'lastProcessId': 10031073,
                    'lastProcessStartTime': '2018-06-05T20:20:53',
                    'lastProcessStatus': 'success',
                    'pipelineDisplayName': 'WAZP',
                    'pipelineId': 214,
                    'pipelineName': 'wazp_new',
                    'processCount': '1',
                    'stageDisplayName': 'Science Analysis'
                }
            }
        ]
    }
}

snapshots['APITestCase::test_pipelines_no_args 1'] = {
    'pipelinesByStageIdAndTagIdAndFieldId': {
        'edges': [
            {
                'node': {
                    'lastProcessEndTime': '2016-08-30T14:30:11',
                    'lastProcessId': 10024396,
                    'lastProcessStartTime': '2016-08-30T14:29:48',
                    'lastProcessStatus': 'success',
                    'pipelineDisplayName': 'Install Catalogs',
                    'pipelineId': 185,
                    'pipelineName': 'install_catalogs',
                    'processCount': '2',
                    'stageDisplayName': 'Data Installation'
                }
            },
            {
                'node': {
                    'lastProcessEndTime': '2018-06-05T20:32:19',
                    'lastProcessId': 10031073,
                    'lastProcessStartTime': '2018-06-05T20:20:53',
                    'lastProcessStatus': 'success',
                    'pipelineDisplayName': 'WAZP',
                    'pipelineId': 214,
                    'pipelineName': 'wazp_new',
                    'processCount': '1',
                    'stageDisplayName': 'Science Analysis'
                }
            }
        ]
    }
}
