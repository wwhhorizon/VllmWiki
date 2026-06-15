# vllm-project/vllm#3952: [Bug]: StableLM 12b head size incorrect

| 字段 | 值 |
| --- | --- |
| Issue | [#3952](https://github.com/vllm-project/vllm/issues/3952) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;model_support |
| 子分类 |  |
| Operator 关键词 | attention;cuda |
| 症状 | mismatch |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: StableLM 12b head size incorrect

### Issue 正文摘录

### Your current environment ```text Can't run since running on dockerized cluster. Using latest pip install for both vLLM and transformers + CUDA 12.1 ``` ### 🐛 Describe the bug Running vLLM with the new StableLM model `stabilityai/stablelm-2-12b` leads to this error regarding head size. ``` 2024-04-09T23:20:46Z [job] File "/workspace/miniconda3/envs/py3.10/lib/python3.10/site-packages/vllm/engine/ray_utils.py", line 45, in execute_method 2024-04-09T23:20:46Z [job] raise e 2024-04-09T23:20:46Z [job] File "/workspace/miniconda3/envs/py3.10/lib/python3.10/site-packages/vllm/engine/ray_utils.py", line 37, in execute_method 2024-04-09T23:20:46Z [job] return executor(*args, **kwargs) 2024-04-09T23:20:46Z [job] File "/workspace/miniconda3/envs/py3.10/lib/python3.10/site-packages/vllm/worker/worker.py", line 107, in load_model 2024-04-09T23:20:46Z [job] self.model_runner.load_model() 2024-04-09T23:20:46Z [job] File "/workspace/miniconda3/envs/py3.10/lib/python3.10/site-packages/vllm/worker/model_runner.py", line 95, in load_model 2024-04-09T23:20:46Z [job] self.model = get_model( 2024-04-09T23:20:46Z [job] File "/workspace/miniconda3/envs/py3.10/lib/python3.10/site-packages/vllm/model_e...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: g;stale ### Your current environment ```text Can't run since running on dockerized cluster. Using latest pip install for both vLLM and transformers + CUDA 12.1 ``` ### 🐛 Describe the bug Running vLLM with the new Stable...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: UDA 12.1 ``` ### 🐛 Describe the bug Running vLLM with the new StableLM model `stabilityai/stablelm-2-12b` leads to this error regarding head size. ``` 2024-04-09T23:20:46Z [job] File "/workspace/miniconda3/envs/py3.10/l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rized cluster. Using latest pip install for both vLLM and transformers + CUDA 12.1 ``` ### 🐛 Describe the bug Running vLLM with the new StableLM model `stabilityai/stablelm-2-12b` leads to this error regarding head size...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: StableLM 12b head size incorrect bug;stale ### Your current environment ```text Can't run since running on dockerized cluster. Using latest pip install for both vLLM and transformers + CUDA 12.1 ``` ### 🐛 Describ...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: space/miniconda3/envs/py3.10/lib/python3.10/site-packages/vllm/attention/backends/flash_attn.py", line 148, in __init__ 2024-04-09T23:20:46Z [job] raise ValueError( 2024-04-09T23:20:46Z [job] ValueError: Head size 160 i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
