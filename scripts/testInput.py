./scripts/oe-build-perf-report -r "~/github/neighbourhoodie/yocto-buildstats" --branch "master" --commit "663f1805742" --branch2 "master" --html

# print_html_report(data, index_l - index_0, buildstats)
import sys
import json
from collections import namedtuple
from oe_build_perf_report import print_html_report

def main(argv=None):
    json1 = """
    {
        "tests": {
            "test1": {
                "name": "test1",
                "description": "Build core-image-sato",
                "status": "SUCCESS",
                "start_time": 1705482088.546597,
                "elapsed_time": 5112.616672,
                "measurements": {
                    "build": {
                        "type": "sysres",
                        "name": "build",
                        "legend": "bitbake core-image-sato",
                        "values": {
                            "start_time": 1705482159.714656,
                            "elapsed_time": 4853.825747,
                            "rusage": {
                                "ru_utime": 58.186712,
                                "ru_stime": 6.494605,
                                "ru_maxrss": 60204,
                                "ru_minflt": 57991,
                                "ru_majflt": 49,
                                "ru_inblock": 36808,
                                "ru_oublock": 6568,
                                "ru_nvcsw": 356243,
                                "ru_nivcsw": 809
                            },
                            "iostat": {
                                "rchar": 100822040,
                                "wchar": 5588997,
                                "syscr": 334151,
                                "syscw": 56861,
                                "read_bytes": 18845696,
                                "write_bytes": 3362816,
                                "cancelled_write_bytes": 0
                            }
                        }
                    },
                    "tmpdir": {
                        "type": "diskusage",
                        "name": "tmpdir",
                        "legend": "tmpdir",
                        "values": {
                            "size": 93293692
                        }
                    },
                    "rootfs": {
                        "type": "diskusage",
                        "name": "rootfs",
                        "legend": "rootfs",
                        "values": {
                            "size": 340424
                        }
                    }
                }
            }
        }
    }
    """
    json2= """
    {
        "metadata": {},
        "tests": {
                "test1": {
                "name": "test1",
                "description": "Build core-image-sato",
                "status": "SUCCESS",
                "start_time": 1705460491.248447,
                "elapsed_time": 5087.892004,
                "measurements": {
                    "build": {
                        "type": "sysres",
                        "name": "build",
                        "legend": "bitbake core-image-sato",
                        "values": {
                            "start_time": 1705460559.983171,
                            "elapsed_time": 4828.072535,
                            "rusage": {
                                "ru_utime": 58.901703,
                                "ru_stime": 6.572947,
                                "ru_maxrss": 57500,
                                "ru_minflt": 50203,
                                "ru_majflt": 47,
                                "ru_inblock": 36984,
                                "ru_oublock": 6568,
                                "ru_nvcsw": 342128,
                                "ru_nivcsw": 1452
                            },
                            "iostat": {
                                "rchar": 100815572,
                                "wchar": 5588997,
                                "syscr": 333972,
                                "syscw": 56861,
                                "read_bytes": 18935808,
                                "write_bytes": 3362816,
                                "cancelled_write_bytes": 0
                            }
                        }
                    },
                    "tmpdir": {
                        "type": "diskusage",
                        "name": "tmpdir",
                        "legend": "tmpdir",
                        "values": {
                            "size": 93293640
                        }
                    },
                    "rootfs": {
                        "type": "diskusage",
                        "name": "rootfs",
                        "legend": "rootfs",
                        "values": {
                            "size": 340424
                        }
                    }
                }
            }
        }
    }
    """
    # rawdata1 = '{"metadata":{"hostname":"perf-alma8","distro":{"id":"poky","version_id":"4.3+snapshot-663f1805742ff6fb6955719d0ab7846a425debcf","pretty_name":"poky 4.3+snapshot-663f1805742ff6fb6955719d0ab7846a425debcf"},"host_distro":{"id":"almalinux","version_id":"8.5","pretty_name":"AlmaLinux 8.5 (Arctic Sphynx)"},"layers":{"meta":{"commit":"663f1805742ff6fb6955719d0ab7846a425debcf","commit_count":73124,"branch":"master"},"meta-poky":{"commit":"663f1805742ff6fb6955719d0ab7846a425debcf","commit_count":73124,"branch":"master"},"meta-yocto-bsp":{"commit":"663f1805742ff6fb6955719d0ab7846a425debcf","commit_count":73124,"branch":"master"}},"bitbake":{"commit":"663f1805742ff6fb6955719d0ab7846a425debcf","commit_count":73124,"branch":"master"},"config":{"BB_NUMBER_THREADS":"24","MACHINE":"qemux86","PARALLEL_MAKE":"-j 24"}},"tester_host":"perf-alma8","start_time":1705460491.248104,"elapsed_time":15284.451595,"tests":{"test1":{"name":"test1","description":"Build core-image-sato","status":"SUCCESS","start_time":1705460491.248447,"elapsed_time":5087.892004,"measurements":{"build":{"type":"sysres","name":"build","legend":"bitbake core-image-sato","values":{"start_time":1705460559.983171,"elapsed_time":4828.072535,"rusage":{"ru_utime":58.901703,"ru_stime":6.572947,"ru_maxrss":57500,"ru_minflt":50203,"ru_majflt":47,"ru_inblock":36984,"ru_oublock":6568,"ru_nvcsw":342128,"ru_nivcsw":1452},"iostat":{"rchar":100815572,"wchar":5588997,"syscr":333972,"syscw":56861,"read_bytes":18935808,"write_bytes":3362816,"cancelled_write_bytes":0}}},"tmpdir":{"type":"diskusage","name":"tmpdir","legend":"tmpdir","values":{"size":93293640}},"rootfs":{"type":"diskusage","name":"rootfs","legend":"rootfs","values":{"size":340424}}}},"test12":{"name":"test12","description":"Build virtual/kernel","status":"SUCCESS","start_time":1705465579.140645,"elapsed_time":895.690519,"measurements":{"build":{"type":"sysres","name":"build","legend":"bitbake virtual/kernel","values":{"start_time":1705465696.395422,"elapsed_time":778.284369,"rusage":{"ru_utime":3.688514,"ru_stime":0.590289,"ru_maxrss":92788,"ru_minflt":15199,"ru_majflt":48,"ru_inblock":37608,"ru_oublock":256,"ru_nvcsw":22977,"ru_nivcsw":96},"iostat":{"rchar":13486583,"wchar":98684,"syscr":13098,"syscw":249,"read_bytes":19255296,"write_bytes":131072,"cancelled_write_bytes":0}}}}},"test13":{"name":"test13","description":"Build core-image-sato with rm_work enabled","status":"SUCCESS","start_time":1705466474.831579,"elapsed_time":6605.878232,"measurements":{"build":{"type":"sysres","name":"build","legend":"bitbakecore-image-sato","values":{"start_time":1705468185.849928,"elapsed_time":4889.183282,"rusage":{"ru_utime":58.768916,"ru_stime":6.735194,"ru_maxrss":92788,"ru_minflt":51535,"ru_majflt":48,"ru_inblock":37928,"ru_oublock":7048,"ru_nvcsw":357449,"ru_nivcsw":878},"iostat":{"rchar":103872009,"wchar":6040594,"syscr":344181,"syscw":61405,"read_bytes":19419136,"write_bytes":3608576,"cancelled_write_bytes":0}}},"tmpdir":{"type":"diskusage","name":"tmpdir","legend":"tmpdir","values":{"size":16927420}}}},"test2":{"name":"test2","description":"Run core-image-sato do_rootfs with sstate","status":"SUCCESS","start_time":1705473080.71016,"elapsed_time":616.122811,"measurements":{"do_rootfs":{"type":"sysres","name":"do_rootfs","legend":"bitbake do_rootfs","values":{"start_time":1705473374.2632,"elapsed_time":322.490196,"rusage":{"ru_utime":7.541031,"ru_stime":1.105109,"ru_maxrss":129652,"ru_minflt":20477,"ru_majflt":48,"ru_inblock":37456,"ru_oublock":2336,"ru_nvcsw":66121,"ru_nivcsw":149},"iostat":{"rchar":21857986,"wchar":2260981,"syscr":53967,"syscw":20016,"read_bytes":19177472,"write_bytes":1196032,"cancelled_write_bytes":0}}}}},"test3":{"name":"test3","description":"Bitbake parsing (bitbake -p)","status":"SUCCESS","start_time":1705473696.833395,"elapsed_time":61.551663,"measurements":{"parse_1":{"type":"sysres","name":"parse_1","legend":"bitbake -p (no caches)","values":{"start_time":1705473696.856718,"elapsed_time":30.773411,"rusage":{"ru_utime":0.915864,"ru_stime":0.12360299999999999,"ru_maxrss":129652,"ru_minflt":13036,"ru_majflt":0,"ru_inblock":0,"ru_oublock":144,"ru_nvcsw":616,"ru_nivcsw":5},"iostat":{"rchar":10918400,"wchar":77609,"syscr":1249,"syscw":32,"read_bytes":0,"write_bytes":73728,"cancelled_write_bytes":0}}},"parse_2":{"type":"sysres","name":"parse_2","legend":"bitbake -p (no tmp/cache)","values":{"start_time":1705473727.644352,"elapsed_time":26.41401,"rusage":{"ru_utime":0.9556469999999999,"ru_stime":0.106227,"ru_maxrss":129652,"ru_minflt":13049,"ru_majflt":0,"ru_inblock":0,"ru_oublock":144,"ru_nvcsw":506,"ru_nivcsw":6},"iostat":{"rchar":10918400,"wchar":77609,"syscr":1249,"syscw":32,"read_bytes":0,"write_bytes":73728,"cancelled_write_bytes":0}}},"parse_3":{"type":"sysres","name":"parse_3","legend":"bitbake -p (cached)","values":{"start_time":1705473754.071995,"elapsed_time":4.305491,"rusage":{"ru_utime":1.366023,"ru_stime":0.19899599999999998,"ru_maxrss":129652,"ru_minflt":18640,"ru_majflt":0,"ru_inblock":0,"ru_oublock":144,"ru_nvcsw":4782,"ru_nivcsw":4},"iostat":{"rchar":11153170,"wchar":77484,"syscr":4737,"syscw":30,"read_bytes":0,"write_bytes":73728,"cancelled_write_bytes":0}}}}},"test4":{"name":"test4","description":"eSDK metrics","status":"SUCCESS","start_time":1705473758.385362,"elapsed_time":2017.314051,"measurements":{"installer_bin":{"type":"diskusage","name":"installer_bin","legend":"eSDK installer","values":{"size":416816}},"deploy":{"type":"sysres","name":"deploy","legend":"eSDK deploy","values":{"start_time":1705475647.809116,"elapsed_time":112.934672,"rusage":{"ru_utime":27.681674,"ru_stime":11.322006,"ru_maxrss":130276,"ru_minflt":343243,"ru_majflt":60,"ru_inblock":921842,"ru_oublock":1461264,"ru_nvcsw":133916,"ru_nivcsw":1242},"iostat":{"rchar":2473447688,"wchar":2335680885,"syscr":408775,"syscw":2059809,"read_bytes":471983104,"write_bytes":748167168,"cancelled_write_bytes":69697536}}},"deploy_dir":{"type":"diskusage","name":"deploy_dir","legend":"deploy dir","values":{"size":2372734}}}}}}'
    # rawdata2 = '{"metadata":{"hostname":"perf-alma8","distro":{"id":"poky","version_id":"4.3+snapshot-663f1805742ff6fb6955719d0ab7846a425debcf","pretty_name":"poky 4.3+snapshot-663f1805742ff6fb6955719d0ab7846a425debcf"},"host_distro":{"id":"almalinux","version_id":"8.5","pretty_name":"AlmaLinux 8.5 (Arctic Sphynx)"},"layers":{"meta":{"commit":"663f1805742ff6fb6955719d0ab7846a425debcf","commit_count":73124,"branch":"master"},"meta-poky":{"commit":"663f1805742ff6fb6955719d0ab7846a425debcf","commit_count":73124,"branch":"master"},"meta-yocto-bsp":{"commit":"663f1805742ff6fb6955719d0ab7846a425debcf","commit_count":73124,"branch":"master"}},"bitbake":{"commit":"663f1805742ff6fb6955719d0ab7846a425debcf","commit_count":73124,"branch":"master"},"config":{"BB_NUMBER_THREADS":"24","MACHINE":"qemux86","PARALLEL_MAKE":"-j 24"}},"tester_host":"perf-alma8","start_time":1705482088.546527,"elapsed_time":15268.316039,"tests":{"test1":{"name":"test1","description":"Build core-image-sato","status":"SUCCESS","start_time":1705482088.546597,"elapsed_time":5112.616672,"measurements":{"build":{"type":"sysres","name":"build","legend":"bitbake core-image-sato","values":{"start_time":1705482159.714656,"elapsed_time":4853.825747,"rusage":{"ru_utime":58.186712,"ru_stime":6.494605,"ru_maxrss":60204,"ru_minflt":57991,"ru_majflt":49,"ru_inblock":36808,"ru_oublock":6568,"ru_nvcsw":356243,"ru_nivcsw":809},"iostat":{"rchar":100822040,"wchar":5588997,"syscr":334151,"syscw":56861,"read_bytes":18845696,"write_bytes":3362816,"cancelled_write_bytes":0}}},"tmpdir":{"type":"diskusage","name":"tmpdir","legend":"tmpdir","values":{"size":93293692}},"rootfs":{"type":"diskusage","name":"rootfs","legend":"rootfs","values":{"size":340424}}}},"test12":{"name":"test12","description":"Build virtual/kernel","status":"SUCCESS","start_time":1705487201.163446,"elapsed_time":895.964147,"measurements":{"build":{"type":"sysres","name":"build","legend":"bitbake virtual/kernel","values":{"start_time":1705487318.03102,"elapsed_time":779.090505,"rusage":{"ru_utime":3.793851,"ru_stime":0.557581,"ru_maxrss":94468,"ru_minflt":16686,"ru_majflt":48,"ru_inblock":38408,"ru_oublock":264,"ru_nvcsw":22342,"ru_nivcsw":163},"iostat":{"rchar":13486657,"wchar":98684,"syscr":13098,"syscw":249,"read_bytes":19664896,"write_bytes":135168,"cancelled_write_bytes":0}}}}},"test13":{"name":"test13","description":"Build core-image-sato with rm_work enabled","status":"SUCCESS","start_time":1705488097.127843,"elapsed_time":6602.023517,"measurements":{"build":{"type":"sysres","name":"build","legend":"bitbakecore-image-sato","values":{"start_time":1705489842.033998,"elapsed_time":4852.781268,"rusage":{"ru_utime":60.9161,"ru_stime":6.928066,"ru_maxrss":95444,"ru_minflt":59624,"ru_majflt":48,"ru_inblock":38832,"ru_oublock":7024,"ru_nvcsw":360218,"ru_nivcsw":1098},"iostat":{"rchar":103863258,"wchar":6040620,"syscr":344155,"syscw":61406,"read_bytes":19881984,"write_bytes":3596288,"cancelled_write_bytes":0}}},"tmpdir":{"type":"diskusage","name":"tmpdir","legend":"tmpdir","values":{"size":16927288}}}},"test2":{"name":"test2","description":"Run core-image-sato do_rootfs with sstate","status":"SUCCESS","start_time":1705494699.152096,"elapsed_time":622.704574,"measurements":{"do_rootfs":{"type":"sysres","name":"do_rootfs","legend":"bitbake do_rootfs","values":{"start_time":1705494998.619551,"elapsed_time":323.156494,"rusage":{"ru_utime":8.112031,"ru_stime":1.217849,"ru_maxrss":133220,"ru_minflt":20435,"ru_majflt":48,"ru_inblock":38344,"ru_oublock":2336,"ru_nvcsw":70525,"ru_nivcsw":169},"iostat":{"rchar":21857971,"wchar":2260979,"syscr":53966,"syscw":20016,"read_bytes":19632128,"write_bytes":1196032,"cancelled_write_bytes":0}}}}},"test3":{"name":"test3","description":"Bitbake parsing (bitbake -p)","status":"SUCCESS","start_time":1705495321.857099,"elapsed_time":60.716604,"measurements":{"parse_1":{"type":"sysres","name":"parse_1","legend":"bitbake -p (no caches)","values":{"start_time":1705495321.881146,"elapsed_time":28.493524,"rusage":{"ru_utime":0.7913709999999999,"ru_stime":0.10388599999999999,"ru_maxrss":131260,"ru_minflt":13029,"ru_majflt":0,"ru_inblock":0,"ru_oublock":144,"ru_nvcsw":549,"ru_nivcsw":7},"iostat":{"rchar":10918400,"wchar":77609,"syscr":1249,"syscw":32,"read_bytes":0,"write_bytes":73728,"cancelled_write_bytes":0}}},"parse_2":{"type":"sysres","name":"parse_2","legend":"bitbake -p (no tmp/cache)","values":{"start_time":1705495350.388994,"elapsed_time":27.218119,"rusage":{"ru_utime":0.5038279999999999,"ru_stime":0.082259,"ru_maxrss":131260,"ru_minflt":13028,"ru_majflt":0,"ru_inblock":0,"ru_oublock":144,"ru_nvcsw":657,"ru_nivcsw":4},"iostat":{"rchar":10918400,"wchar":77609,"syscr":1249,"syscw":32,"read_bytes":0,"write_bytes":73728,"cancelled_write_bytes":0}}},"parse_3":{"type":"sysres","name":"parse_3","legend":"bitbake -p (cached)","values":{"start_time":1705495377.622559,"elapsed_time":4.942792,"rusage":{"ru_utime":1.385748,"ru_stime":0.189604,"ru_maxrss":131260,"ru_minflt":18654,"ru_majflt":0,"ru_inblock":0,"ru_oublock":144,"ru_nvcsw":5070,"ru_nivcsw":9},"iostat":{"rchar":11153167,"wchar":77484,"syscr":4737,"syscw":30,"read_bytes":0,"write_bytes":73728,"cancelled_write_bytes":0}}}}},"test4":{"name":"test4","description":"eSDK metrics","status":"SUCCESS","start_time":1705495382.574114,"elapsed_time":1974.288017,"measurements":{"installer_bin":{"type":"diskusage","name":"installer_bin","legend":"eSDK installer","values":{"size":416783}},"deploy":{"type":"sysres","name":"deploy","legend":"eSDK deploy","values":{"start_time":1705497228.837466,"elapsed_time":114.065528,"rusage":{"ru_utime":27.967811,"ru_stime":11.498602,"ru_maxrss":131516,"ru_minflt":343063,"ru_majflt":59,"ru_inblock":915218,"ru_oublock":1461200,"ru_nvcsw":134283,"ru_nivcsw":1266},"iostat":{"rchar":2473224253,"wchar":2335494159,"syscr":403155,"syscw":2059636,"read_bytes":468591616,"write_bytes":748134400,"cancelled_write_bytes":69668864}}},"deploy_dir":{"type":"diskusage","name":"deploy_dir","legend":"deploy dir","values":{"size":2372759}}}}}}'
    data1 = json.loads(json1)
    data2 = json.loads(json2)
    y = namedtuple('AggregateTestData', ['metadata', 'results'])
    data = [data1, data2]
    print("+++++++++ ", data)
    buildstats = None
    print_html_report(data, 1, buildstats)

if __name__ == '__main__':
    sys.exit(main())
