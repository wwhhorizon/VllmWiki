# vllm-project/vllm#5779: [Bug]: 使用vllm+ray分布式推理报错

| 字段 | 值 |
| --- | --- |
| Issue | [#5779](https://github.com/vllm-project/vllm/issues/5779) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 使用vllm+ray分布式推理报错

### Issue 正文摘录

### Your current environment Python==3.10.14 vllm==0.5.0.post1 ray==2.24.0 Node status --------------------------------------------------------------- Active: 1 node_37c2b26800cc853721ef351ca107c298ae77efcb5504d8e0c900ed1d 1 node_62d48658974f4114465450f53fd97c10fcfe6d40b4e896a90a383682 Pending: (no pending nodes) Recent failures: (no failures) Resources --------------------------------------------------------------- Usage: 0.0/52.0 CPU 0.0/2.0 GPU 0B/9.01GiB memory 0B/4.14GiB object_store_memory Demands: (no resource demands) ### 🐛 Describe the bug 在使用 Gloo 进行全网格连接时遇到了问题，没有找到解决办法 脚本如下： from vllm import LLM prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] llm = LLM(model="/mnt/d/llm/qwen/qwen1.5_0.5b", trust_remote_code=True, gpu_memory_utilization=0.4,enforce_eager=True,tensor_parallel_size=2,swap_space=1) outputs = llm.generate(prompts) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") 报错如下： [rank0]: Traceback (most recent call last): [rank0]: File "/data/vllm_test.py", line 13, in [rank0]: llm = LLM(mod...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: pital of France is", "The future of AI is", ] llm = LLM(model="/mnt/d/llm/qwen/qwen1.5_0.5b", trust_remote_code=True, gpu_memory_utilization=0.4,enforce_eager=True,tensor_parallel_size=2,swap_space=1) outputs = llm.gene...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: in __init__ [rank0]: cpu_group = torch.distributed.new_group(ranks, backend="gloo") [rank0]: File "/home/jky/miniconda3/envs/ray/lib/python3.10/site-packages/torch/distributed/c10d_logger.py", line 89, in wrapper [rank0...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ### 🐛 Describe the bug 在使用 Gloo 进行全网格连接时遇到了问题，没有找到解决办法 脚本如下： from vllm import LLM prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] llm = LLM(...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: 使用vllm+ray分布式推理报错 bug;stale ### Your current environment Python==3.10.14 vllm==0.5.0.post1 ray==2.24.0 Node status --------------------------------------------------------------- Active: 1 node_37c2b26800cc853721...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [rank0]: Traceback (most recent call last): [rank0]: File "/data/vllm_test.py", line 13, in [rank0]: llm = LLM(model="/mnt/d/llm/qwen/qwen1.5_0.5b", trust_remote_code=True, gpu_memory_utilization=0.4,enforce_eager=True,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
