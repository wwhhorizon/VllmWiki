# vllm-project/vllm#1602: LLMEngine.step() missing 1 required positional argument: 'request_arrival_time'

| 字段 | 值 |
| --- | --- |
| Issue | [#1602](https://github.com/vllm-project/vllm/issues/1602) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 | debug |
| Operator 关键词 | cuda;sampling |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> LLMEngine.step() missing 1 required positional argument: 'request_arrival_time'

### Issue 正文摘录

vllm==0.1.3 ray==2.8.0 ` from vllm import LLM, SamplingParams prompts = [ "Funniest joke ever:", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.95, top_p=0.95, max_tokens=200) llm = LLM(model="xxx", tensor_parallel_size=2) **outputs = llm.generate(prompts, sampling_params)** print(outputs) ` error message ` (pid=27540) INFO: Init log file success, log_file=/apps/logs/log_receiver/rec-pred-2-mlp-pytorch-1029026.ai.vip.com/vllm.log (RayWorker pid=27540) [W socket.cpp:436] [c10d] The server socket cannot be initialized on [::]:49363 (errno: 97 - Address family not supported by protocol). (RayWorker pid=27540) [W socket.cpp:663] [c10d] The client socket cannot be initialized to connect to [pytorch-rec-pred-2-mlp-1029026-worker-0.pytorch-rec-pred-2-mlp-1029026.mlp.svc.gd17-ai-001.vip.com]:49363 (errno: 97 - Address family not supported by protocol). (RayWorker pid=27540) /opt/conda/lib/python3.10/site-packages/vllm/worker/worker.py:231: UserWarning: The torch.cuda.*DtypeTensor constructors are no longer recommended. It's best to use methods such as torch.tensor(data, dtype=*, device='cuda') to create tensors. (Triggered internally at...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: nal argument: 'request_arrival_time' vllm==0.1.3 ray==2.8.0 ` from vllm import LLM, SamplingParams prompts = [ "Funniest joke ever:", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 10/site-packages/vllm/worker/worker.py:231: UserWarning: The torch.cuda.*DtypeTensor constructors are no longer recommended. It's best to use methods such as torch.tensor(data, dtype=*, device='cuda') to create tensors....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: thon3.10/site-packages/vllm/worker/worker.py:231: UserWarning: The torch.cuda.*DtypeTensor constructors are no longer recommended. It's best to use methods such as torch.tensor(data, dtype=*, device='cuda') to create te...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: = SamplingParams(temperature=0.95, top_p=0.95, max_tokens=200) llm = LLM(model="xxx", tensor_parallel_size=2) **outputs = llm.generate(prompts, sampling_params)** print(outputs) ` error message ` (pid=27540) INFO: Init...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: LLMEngine.step() missing 1 required positional argument: 'request_arrival_time' vllm==0.1.3 ray==2.8.0 ` from vllm import LLM, SamplingParams prompts = [ "Funniest joke ever:", "The capital of France is", "The future of...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
