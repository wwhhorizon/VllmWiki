# vllm-project/vllm#25229: [Bug]: Deepseek vl2 model decoding phase has a very worse performance in both online and offline inference

| 字段 | 值 |
| --- | --- |
| Issue | [#25229](https://github.com/vllm-project/vllm/issues/25229) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;sampling_logits |
| 子分类 | throughput |
| Operator 关键词 | cuda |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deepseek vl2 model decoding phase has a very worse performance in both online and offline inference

### Issue 正文摘录

### Your current environment We use deepseek_vl2_tiny model with only 3B weights, the throughput in decoding phase is less than 100 for a single prompt, and using CUDA graph performs worse than not using CUDA graph. ### 🐛 Describe the bug from vllm import LLM, EngineArgs, SamplingParams from PIL import Image import torch from dataclasses import asdict import time model_name = "deepseek-ai/deepseek-vl2-tiny" engine_args = EngineArgs( model=model_name, max_model_len=4096, max_num_seqs=1, hf_overrides={"architectures": ["DeepseekVLV2ForCausalLM"]}, limit_mm_per_prompt={"image": 1}, enforce_eager=True #False ) engine_args = asdict(engine_args) | { "seed": None, # "mm_processor_cache_gb": 0 if args.disable_mm_processor_cache else 4, } llm = LLM(**engine_args) data = Image.open("/home/admin/workspace/aop_lab/app_source/q0.jpeg") img_questions = [ "提供了商品的基本外观信息. \n 山姆超市 海盐苏打饼干1.5kg 休闲零食点心 正品代购 请简要描述一下此商品的相关属性。", ] prompts = [ f" : \nPlease describe this picture\n\n :" ] inputs = [ { "prompt": prompts[i % len(prompts)], "multi_modal_data": {'image': data}, } for i in range(len(prompts)) ] stop_token_ids = [93532, 93653, 944, 93421, 1019, 93653, 93519] # stop_token_ids=None sampling_params...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: orms worse than not using CUDA graph. ### 🐛 Describe the bug from vllm import LLM, EngineArgs, SamplingParams from PIL import Image import torch from dataclasses import asdict import time model_name = "deepseek-ai/deeps...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ughput in decoding phase is less than 100 for a single prompt, and using CUDA graph performs worse than not using CUDA graph. ### 🐛 Describe the bug from vllm import LLM, EngineArgs, SamplingParams from PIL import Image...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Deepseek vl2 model decoding phase has a very worse performance in both online and offline inference bug;stale ### Your current environment We use deepseek_vl2_tiny model with only 3B weights, the throughput in de...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: nt environment We use deepseek_vl2_tiny model with only 3B weights, the throughput in decoding phase is less than 100 for a single prompt, and using CUDA graph performs worse than not using CUDA graph. ### 🐛 Describe th...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: alLM"]}, limit_mm_per_prompt={"image": 1}, enforce_eager=True #False ) engine_args = asdict(engine_args) | { "seed": None, # "mm_processor_cache_gb": 0 if args.disable_mm_processor_cache else 4, } llm = LLM(**engine_arg...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
