# vllm-project/vllm#18983: [Bug]: Failed to load the fine-tuned Qwen2.5-VL-7B-Instruct model.

| 字段 | 值 |
| --- | --- |
| Issue | [#18983](https://github.com/vllm-project/vllm/issues/18983) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failed to load the fine-tuned Qwen2.5-VL-7B-Instruct model.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I want to load this model which is exported from `llama-factory`: ![Image](https://github.com/user-attachments/assets/91c6d98c-0a4f-4822-8175-5421fc81e7e1) Using this script: ```python llm = LLM( model=self.model_name, gpu_memory_utilization=gpu_memory_utilization, max_model_len=max_model_len, download_dir=download_dir, dtype=dtype, limit_mm_per_prompt={"image": 10}, allowed_local_media_path="/", **kwargs, ) ``` Then I got this error: ```bash Traceback (most recent call last): File "/mlcv3/WorkingSpace/Personal/baotg/AICity25/Track2/src/inference/new_inference.py", line 176, in main(args) File "/mlcv3/WorkingSpace/Personal/baotg/AICity25/Track2/src/inference/new_inference.py", line 106, in main model = load_model(args) File "/mlcv3/WorkingSpace/Personal/baotg/AICity25/Track2/src/inference/new_inference.py", line 78, in load_model return VLLM( File "/mlcv3/WorkingSpace/Personal/baotg/AICity25/Track2/src/models/vllm_generator.py", line 21, in __init__ self.llm = LLM( File "/root/miniconda3/envs/main/lib/python3.10/site-packages/vllm/utils.py", line 1022, in inner return fn(*args, **kwargs) File "/root/miniconda3/envs/main/lib/pytho...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Failed to load the fine-tuned Qwen2.5-VL-7B-Instruct model. bug ### Your current environment ### 🐛 Describe the bug I want to load this model which is exported from `llama-factory`: ![Image](https://github.com/us...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ck (most recent call last): File "/mlcv3/WorkingSpace/Personal/baotg/AICity25/Track2/src/inference/new_inference.py", line 176, in main(args) File "/mlcv3/WorkingSpace/Personal/baotg/AICity25/Track2/src/inference/new_in...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: max_model_len=max_model_len, download_dir=download_dir, dtype=dtype, limit_mm_per_prompt={"image": 10}, allowed_local_media_path="/", **kwargs, ) ``` Then I got this error: ```bash Traceback (most recent call last): Fil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ontend_api;hardware_porting;model_support;quantization cuda;quantization;triton build_error;crash dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
