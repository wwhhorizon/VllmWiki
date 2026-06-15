# vllm-project/vllm#9870: [Bug]: LLaVA-v1.5-13B with OpenAI compatible API reported an error

| 字段 | 值 |
| --- | --- |
| Issue | [#9870](https://github.com/vllm-project/vllm/issues/9870) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LLaVA-v1.5-13B with OpenAI compatible API reported an error

### Issue 正文摘录

### Your current environment ### Model Input Dumps [err_execute_model_input_20241031-063903.zip](https://github.com/user-attachments/files/17583274/err_execute_model_input_20241031-063903.zip) ### 🐛 Describe the bug I succeed in starting llava-hf/llava-1.5-13b-hf server, but get the problem below when running on mmbench samples ``` Traceback (most recent call last): ERROR 10-31 06:39:03 engine.py:158] File "/data2/ligeng/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/mul tiprocessing/engine.py", line 156, in start ERROR 10-31 06:39:03 engine.py:158] self.run_engine_loop() ERROR 10-31 06:39:03 engine.py:158] File "/data2/ligeng/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/mul tiprocessing/engine.py", line 219, in run_engine_loop ERROR 10-31 06:39:03 engine.py:158] request_outputs = self.engine_step() ERROR 10-31 06:39:03 engine.py:158] File "/data2/ligeng/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/mul tiprocessing/engine.py", line 237, in engine_step ERROR 10-31 06:39:03 engine.py:158] raise e ERROR 10-31 06:39:03 engine.py:158] File "/data2/ligeng/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/mul tiprocessing/engin...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ompatible API reported an error bug ### Your current environment ### Model Input Dumps [err_execute_model_input_20241031-063903.zip](https://github.com/user-attachments/files/17583274/err_execute_model_input_20241031-06...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;speculative_decoding cuda;operator;triton build_error;cra...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e ns to 0 placeholders** ``` The command i use is like: ``` gpu_list="${CUDA_VISIBLE_DEVICES:-0}" IFS=',' read -ra GPULIST <<< "$gpu_list" port=$((8000 + ${GPULIST[0]})) vllm serve llava-hf/llava-1.5-13b-hf --port $port...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ERROR 10-31 06:39:03 engine.py:158] request_outputs = self.engine_step() ERROR 10-31 06:39:03 engine.py:158] File "/data2/ligeng/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/mul tiprocessing
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _porting;model_support;multimodal_vlm;speculative_decoding cuda;operator;triton build_error;crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
