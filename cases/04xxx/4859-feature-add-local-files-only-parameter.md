# vllm-project/vllm#4859: [Feature]: add local_files_only parameter

| 字段 | 值 |
| --- | --- |
| Issue | [#4859](https://github.com/vllm-project/vllm/issues/4859) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: add local_files_only parameter

### Issue 正文摘录

### 🚀 The feature, motivation and pitch hello, wondering if it is possible to add `local_files_only ` parameter into the following code to load model only from local path. ``` from vllm import LLM, SamplingParams llm = LLM(model= model_local_path) ``` currently, it seems needs to get connection to huggingface.co. > Traceback (most recent call last): > File "/vol/chenyanan/TravelPlanner/tools/planner/inference.py", line 150, in > llm = LLM(model= model_local_path, enable_lora = True, max_lora_rank=64, dtype='float16') > File "/home/chenyanan/anaconda3/envs/tp/lib/python3.9/site-packages/vllm/entrypoints/llm.py", line 112, in __init__ > self.llm_engine = LLMEngine.from_engine_args( > File "/home/chenyanan/anaconda3/envs/tp/lib/python3.9/site-packages/vllm/engine/llm_engine.py", line 173, in from_engine_args > engine_configs = engine_args.create_engine_configs() > File "/home/chenyanan/anaconda3/envs/tp/lib/python3.9/site-packages/vllm/engine/arg_utils.py", line 382, in create_engine_configs > model_config = ModelConfig( > File "/home/chenyanan/anaconda3/envs/tp/lib/python3.9/site-packages/vllm/config.py", line 120, in __init__ > self.hf_config = get_config(self.model, trust_remote_c...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ble to add `local_files_only ` parameter into the following code to load model only from local path. ``` from vllm import LLM, SamplingParams llm = LLM(model= model_local_path) ``` currently, it seems needs to get conne...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: llm = LLM(model= model_local_path, enable_lora = True, max_lora_rank=64, dtype='float16') > File "/home/chenyanan/anaconda3/envs/tp/lib/python3.9/site-packages/vllm/entrypoints/llm.py", line 112, in __init__ > self.llm_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nto the following code to load model only from local path. ``` from vllm import LLM, SamplingParams llm = LLM(model= model_local_path) ``` currently, it seems needs to get connection to huggingface.co. > Traceback (most...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: s/huggingface_hub/file_download.py", line 1261, in hf_hub_download > metadata = get_hf_file_metadata( > File "/home/chenyanan/anaconda3/envs/tp/lib/python3.9/site-packages/huggingface_hub/utils/_validators.py", line 119...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: add local_files_only parameter feature request ### 🚀 The feature, motivation and pitch hello, wondering if it is possible to add `local_files_only ` parameter into the following code to load model only from l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
