# vllm-project/vllm#9153: [Bug]: InternVL bounding box prediction does not work

| 字段 | 值 |
| --- | --- |
| Issue | [#9153](https://github.com/vllm-project/vllm/issues/9153) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: InternVL bounding box prediction does not work

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm starting a vllm container with OpenGVLab/InternVL2 and vLLM version 0.6.2 with `vllm serve OpenGVLab/InternVL2-1B --trust-remote-code` As a prompt, I'm specifically using the object detection prompt: `Please provide the bounding box coordinates of the region this sentence describes: {} `. This prompt is documented [here](https://huggingface.co/OpenGVLab/InternVL2-8B#grounding-benchmarks), [here](https://internvl.readthedocs.io/en/latest/tutorials/faqs.html), or [here](https://github.com/OpenGVLab/InternVL/issues/58). This prompt is designed to make the model output bounding box coordinates. This prompt works correctly when used in `transformers`: ```py path = 'OpenGVLab/InternVL2-1B' model = AutoModel.from_pretrained( path, torch_dtype=torch.bfloat16, low_cpu_mem_usage=True, use_flash_attn=True, trust_remote_code=True ).eval().cuda() tokenizer = AutoTokenizer.from_pretrained(path, trust_remote_code=True, use_fast=False) # set the max number of tiles in `max_num` pixel_values = load_image('./data/image.png', max_num=12).to(torch.bfloat16).cuda() generation_config = dict(max_new_tokens=1024,...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Bug]: InternVL bounding box prediction does not work bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm starting a vllm container with OpenGVLab/InternVL2 and vLLM vers
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: the bug I'm starting a vllm container with OpenGVLab/InternVL2 and vLLM version 0.6.2 with `vllm serve OpenGVLab/InternVL2-1B --trust-remote-code` As a prompt, I'm specifically using the object detection prompt: `Please...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Lab/InternVL2-1B' model = AutoModel.from_pretrained( path, torch_dtype=torch.bfloat16, low_cpu_mem_usage=True, use_flash_attn=True, trust_remote_code=True ).eval().cuda() tokenizer = AutoTokenizer.from_pretrained(path,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: usage=True, use_flash_attn=True, trust_remote_code=True ).eval().cuda() tokenizer = AutoTokenizer.from_pretrained(path, trust_remote_code=True, use_fast=False) # set the max number of tiles in `max_num` pixel_values = l...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ocumented [here](https://huggingface.co/OpenGVLab/InternVL2-8B#grounding-benchmarks), [here](https://internvl.readthedocs.io/en/latest/tutorials/faqs.html), or [here](https://github.com/OpenGVLab/InternVL/issues/58). Th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
