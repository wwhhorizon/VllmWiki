# vllm-project/vllm#24672: [Bug]: GPUModelRunner' object has no attribute 'lora_manager'

| 字段 | 值 |
| --- | --- |
| Issue | [#24672](https://github.com/vllm-project/vllm/issues/24672) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GPUModelRunner' object has no attribute 'lora_manager'

### Issue 正文摘录

### 🐛 Describe the bug Not possible to spin up LoRa adapters with the latest mistral models. ```bash pip list | grep vllm vllm 0.10.1.1 ``` ```bash vllm serve mistralai/Mistral-Small-3.2-24B-Instruct-2506 \ --tokenizer_mode mistral \ --config_format mistral \ --load_format mistral \ --tool-call-parser mistral \ --enable-auto-tool-choice \ --limit-mm-per-prompt '{"image":10}' \ --tensor-parallel-size 2 \ --max-model-len 2048 \ --lora-modules 'myft=/home/tim/lora_adapter' ``` ```bash (VllmWorker TP0 pid=1402898) ERROR 09-11 17:45:52 [multiproc_executor.py:596] WorkerProc hit an exception. (VllmWorker TP0 pid=1402898) ERROR 09-11 17:45:52 [multiproc_executor.py:596] Traceback (most recent call last): (VllmWorker TP0 pid=1402898) ERROR 09-11 17:45:52 [multiproc_executor.py:596] File "/home/tim/anaconda3/envs/torch/lib/python3.10/site-packages/vllm/v1/executor/multiproc_executor.py", line 591, in worker_busy_loop (VllmWorker TP0 pid=1402898) ERROR 09-11 17:45:52 [multiproc_executor.py:596] output = func(*args, **kwargs) (VllmWorker TP0 pid=1402898) ERROR 09-11 17:45:52 [multiproc_executor.py:596] File "/home/tim/anaconda3/envs/torch/lib/python3.10/site-packages/vllm/v1/worker/gpu_worke...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: GPUModelRunner' object has no attribute 'lora_manager' bug ### 🐛 Describe the bug Not possible to spin up LoRa adapters with the latest mistral models. ```bash pip list | grep vllm vllm
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 0.10.1.1 ``` ```bash vllm serve mistralai/Mistral-Small-3.2-24B-Instruct-2506 \ --tokenizer_mode mistral \ --config_format mistral \ --load_format mistral \ --tool-call-parser mistral \ --enable-auto-tool-choice \ --lim...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 2 [multiproc_executor.py:596] return self.model_runner.add_lora(lora_request) (VllmWorker TP0 pid=1402898) ERROR 09-11 17:45:52 [multiproc_executor.py:596] File "/home/tim/anaconda3/envs/torch/lib/python3.10/site-packag...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rypoints/cli/main.py", line 54, in main (APIServer pid=1402460) args.dispatch_function(args) (APIServer pid=1402460) File "/home/tim/anaconda3/envs/torch/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ### 🐛 Describe the bug Not possible to spin up LoRa adapters with the latest mistral models. ```bash pip list | grep vllm vllm 0.10.1.1 ``` ```bash vllm serve mistralai/Mistral-Small-3.2-24B-Instruct-2506 \ --tokenizer_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
