import parsl

from parsl.config import Config
from parsl.providers import AdHocProvider
from parsl.channels import SSHChannel
from parsl.addresses import address_by_query
from parsl.executors import HighThroughputExecutor

from parsl.providers import LocalProvider
from parsl.channels import LocalChannel
from parsl.executors import HighThroughputExecutor

user_opts = {'adhoc':
             {'username': 'clusteruser',
              'script_dir': '/home/clusteruser/parallel-parsl-workflow/',
              'remote_hostnames': ['192.168.1.1','192.168.1.2','192.168.1.3','192.168.1.4','192.168.1.5']
             }
}

remote_htex = Config(
    executors=[
	
        HighThroughputExecutor(
            label='remote_htex',
	    address = '192.168.1.1',
            max_workers=5,
            #address=address_by_query(),
            worker_logdir_root=user_opts['adhoc']['script_dir'],
            provider=AdHocProvider(
                # Command to be run before starting a worker, such as:
                # 'module load Anaconda; source activate parsl_env'.
                worker_init="""
		source /etc/profile
		source ~/.profile
		""",
                channels=[SSHChannel(hostname=m,
                                     username=user_opts['adhoc']['username'],
                                     script_dir=user_opts['adhoc']['script_dir'],
                ) for m in user_opts['adhoc']['remote_hostnames']]
            )
        ),
	HighThroughputExecutor(
            label="htex_Local",
            worker_debug=True,
            cores_per_worker=1,
            provider=LocalProvider(
                channel=LocalChannel(),
                init_blocks=1,
                max_blocks=1,
            ),
        )
    ],
    max_idletime=2.0,
    #  AdHoc Clusters should not be setup with scaling strategy.
    strategy=None,
)
