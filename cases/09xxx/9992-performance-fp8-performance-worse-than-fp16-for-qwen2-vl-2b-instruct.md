# vllm-project/vllm#9992: [Performance]: FP8 performance worse than FP16 for Qwen2-VL-2B-Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#9992](https://github.com/vllm-project/vllm/issues/9992) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | throughput |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: FP8 performance worse than FP16 for Qwen2-VL-2B-Instruct

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance estimated QPS is as follows: bs=1：11.402357925880366 for FP16 and 10.642891382295932 for FP8 bs=8：51.62193861376064 for FP16 and 49.57986576846022 for FP8 bs=16：61.87048607358999 for FP16 and 57.58566218192532 for FP8 bs=32: For FP8: Processed prompts: 100%|████████████████████| 32/32 [00:00<00:00, 67.85it/s, est. speed input: 11468.33 toks/s, output: 271.44 toks/s] For FP16: Processed prompts: 100%|████████████████████| 32/32 [00:00<00:00, 74.14it/s, est. speed input: 12531.11 toks/s, output: 296.59 toks/s] The FP8 model convert script is as follow: ``` from transformers import AutoProcessor, Qwen2VLForConditionalGeneration from llmcompressor.modifiers.quantization import QuantizationModifier from llmcompressor.transformers import oneshot, wrap_hf_model_class MODEL_ID = "/home/hadoop-platcv/qwen2-vl-2b-instruct/00-src-files/00-model/qwen2-vl-2b-instruct/v4-20241028-151341/checkpoint-14427-merged" # Load model. model_class = wrap_hf_model_class(Qwen2VLForConditionalGeneration) model = model_class.from_pretrained(MODEL_ID, device_map="auto", torch_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: oks/s] The FP8 model convert script is as follow: ``` from transformers import AutoProcessor, Qwen2VLForConditionalGeneration from llmcompressor.modifiers.quantization import QuantizationModifier from llmcompressor.tran...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: = processor(text="Hello my name is", return_tensors="pt").input_ids.to("cuda") output = model.generate(input_ids, max_new_tokens=20) print(processor.decode(output[0])) print("==========================================")...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Performance]: FP8 performance worse than FP16 for Qwen2-VL-2B-Instruct performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on perfo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Performance]: FP8 performance worse than FP16 for Qwen2-VL-2B-Instruct performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on perfo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e]: FP8 performance worse than FP16 for Qwen2-VL-2B-Instruct performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance esti...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
