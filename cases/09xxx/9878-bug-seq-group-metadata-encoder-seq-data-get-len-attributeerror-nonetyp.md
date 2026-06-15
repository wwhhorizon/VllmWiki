# vllm-project/vllm#9878: [Bug]: seq_group_metadata.encoder_seq_data.get_len() AttributeError: 'NoneType' object has no attribute 'get_len'

| 字段 | 值 |
| --- | --- |
| Issue | [#9878](https://github.com/vllm-project/vllm/issues/9878) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: seq_group_metadata.encoder_seq_data.get_len() AttributeError: 'NoneType' object has no attribute 'get_len'

### Issue 正文摘录

### Your current environment Due to network isolation, I am currently unable to run scripts. I use 8* h100 80G the run command `vllm serve /models/Llama-3.2-90B-Vision-Instruct/ --dtype auto --tensor_parallel_size 8 --max-num-seqs 32 --enforce-eager --gpu_memory_utilization 0.95 --max_model_len 8192 --max_seq_len_to_capture 8192 --speculative_model "[ngram]" --num_speculative_tokens 5 --ngram_prompt_lookup_max 4 --use_v2_block_manager ` ### Model Input Dumps _No response_ ### 🐛 Describe the bug (VllmWorkerProcess pid=489) ERROR 10-31 08:09:05 multiproc_worker_utils.py:229] Exception in worker VllmWorkerProcess while processing method determine_num_available_blocks. (VllmWorkerProcess pid=489) ERROR 10-31 08:09:05 multiproc_worker_utils.py:229] Traceback (most recent call last): (VllmWorkerProcess pid=489) ERROR 10-31 08:09:05 multiproc_worker_utils.py:229] File "/root/anaconda3/lib/python3.9/site-packages/vllm/executor/multiproc_worker_utils.py", line 223, in _run_worker_process (VllmWorkerProcess pid=489) ERROR 10-31 08:09:05 multiproc_worker_utils.py:229] output = executor(*args, **kwargs) (VllmWorkerProcess pid=489) ERROR 10-31 08:09:05 multiproc_worker_utils.py:229] File "/roo...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: t_len() AttributeError: 'NoneType' object has no attribute 'get_len' bug;stale ### Your current environment Due to network isolation, I am currently unable to run scripts. I use 8* h100 80G the run command `vllm serve /...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Due to network isolation, I am currently unable to run scripts. I use 8* h100 80G the run command `vllm serve /models/Llama-3.2-90B-Vision-Instruct/ --dtype auto --tensor_parallel_size 8 --max-num-seqs 32 --enforce-eage...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: seq_group_metadata.encoder_seq_data.get_len() AttributeError: 'NoneType' object has no attribute 'get_len' bug;stale ### Your current environment Due to network isolation, I am currently unable to run scripts. I...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ly unable to run scripts. I use 8* h100 80G the run command `vllm serve /models/Llama-3.2-90B-Vision-Instruct/ --dtype auto --tensor_parallel_size 8 --max-num-seqs 32 --enforce-eager --gpu_memory_utilization 0.95 --max_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: RROR 10-31 08:09:05 multiproc_worker_utils.py:229] self.model_runner.profile_run() (VllmWorkerProcess pid=489) ERROR 10-31 08:09:05 multiproc_worker_utils.py:229] File "/root/anaconda3/lib/python3.9/site-packages/torch/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
