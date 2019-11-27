import parsl

from parsl.config import Config
from parsl.providers import AdHocProvider
from parsl.channels import SSHChannel
from parsl.addresses import address_by_query
from parsl.executors import HighThroughputExecutor

user_opts = {'adhoc':
             {'username': 'mpiuser',
              'script_dir': '/home/mpiuser/Downloads/TravellingSalesmanProblem-master/PSO-GA/',
              'remote_hostnames': ['10.0.0.2']
             }
}

remote_htex = Config(
    executors=[
	
        HighThroughputExecutor(
            label='remote_htex',
	    address = '127.0.0.1',
            max_workers=2,
            #address=address_by_query(),
            worker_logdir_root=user_opts['adhoc']['script_dir'],
            provider=AdHocProvider(
                # Command to be run before starting a worker, such as:
                # 'module load Anaconda; source activate parsl_env'.
                worker_init='',
                channels=[SSHChannel(hostname=m,
                                     username=user_opts['adhoc']['username'],
                                     script_dir=user_opts['adhoc']['script_dir'],
                ) for m in user_opts['adhoc']['remote_hostnames']]
            )
        )
    ],
    max_idletime=2.0,
    #  AdHoc Clusters should not be setup with scaling strategy.
    strategy=None,
)
