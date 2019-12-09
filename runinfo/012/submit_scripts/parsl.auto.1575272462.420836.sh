
		source /etc/profile
		source ~/.profile
		
process_worker_pool.py  --max_workers=2 -p 0 -c 1.0 -m None --poll 10 --task_url=tcp://10.0.0.1:54607 --result_url=tcp://10.0.0.1:54942 --logdir=/home/mpiuser/Downloads/parallel-parsl-workflow//remote_htex --block_id=0 --hb_period=30 --hb_threshold=120 