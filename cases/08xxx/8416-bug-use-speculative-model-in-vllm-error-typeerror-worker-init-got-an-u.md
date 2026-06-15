# vllm-project/vllm#8416: [Bug]: use speculative model in vllm error: TypeError: Worker.__init__() got an unexpected keyword argument 'num_speculative_tokens'

| 字段 | 值 |
| --- | --- |
| Issue | [#8416](https://github.com/vllm-project/vllm/issues/8416) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: use speculative model in vllm error: TypeError: Worker.__init__() got an unexpected keyword argument 'num_speculative_tokens'

### Issue 正文摘录

### Your current environment vllm = 0.5.4, 0.5.5 ``` super().__init__(*args, **kwargs) File "/usr/local/lib/python3.10/dist-packages/vllm/executor/executor_base.py", line 46, in __init__ self._init_executor() File "/usr/local/lib/python3.10/dist-packages/vllm/executor/multiproc_gpu_executor.py", line 135, in _init_executor self.driver_worker = self._create_worker( File "/usr/local/lib/python3.10/dist-packages/vllm/executor/gpu_executor.py", line 104, in _create_worker return create_worker(**self._get_create_worker_kwargs( File "/usr/local/lib/python3.10/dist-packages/vllm/executor/gpu_executor.py", line 23, in create_worker wrapper.init_worker(**kwargs) File "/usr/local/lib/python3.10/dist-packages/vllm/worker/worker_base.py", line 444, in init_worker self.worker = worker_class(*args, **kwargs) File "/usr/local/lib/python3.10/dist-packages/vllm/spec_decode/spec_decode_worker.py", line 70, in create_spec_worker spec_decode_worker = SpecDecodeWorker.create_worker( File "/usr/local/lib/python3.10/dist-packages/vllm/spec_decode/spec_decode_worker.py", line 161, in create_worker proposer_worker = MultiStepWorker(**draft_worker_kwargs) File "/usr/local/lib/python3.10/dist-packages/vllm/...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: use speculative model in vllm error: TypeError: Worker.__init__() got an unexpected keyword argument 'num_speculative_tokens' bug ### Your current environment vllm = 0.5.4, 0.5.5 ``` super().__init__(*args, **kwa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: use speculative model in vllm error: TypeError: Worker.__init__() got an unexpected keyword argument 'num_speculative_tokens' bug ### Your current environment vllm = 0.5.4, 0.5.5 ``` super().__init__(*args, **kwa...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: vllm ### Model Input Dumps --model "/QwenModel/Qwen2-72B-Instruct-GPTQ-Int4" \ --speculative-model="/QwenModel/Qwen2-1.5B-Instruct" \ --num_speculative_tokens 5 \ --speculative-draft-tensor-parallel-size=1 \ --speculati...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
