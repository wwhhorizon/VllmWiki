# vllm-project/vllm#8097: [Bug]: InternVL2-26B tensor_parallel_size=4, AssertionError: 25 is not divisible by 4

| 字段 | 值 |
| --- | --- |
| Issue | [#8097](https://github.com/vllm-project/vllm/issues/8097) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: InternVL2-26B tensor_parallel_size=4, AssertionError: 25 is not divisible by 4

### Issue 正文摘录

### Your current environment Python3.8 8*A10 GPU Model:InternVL2-26B vllm branch:main torch 2.4.0 torchvision 0.19.0 ### 🐛 Describe the bug ref: https://github.com/vllm-project/vllm/pull/8055#issuecomment-2324237046 https://github.com/vllm-project/vllm/issues/7996 This issue solves some of the inference problems of Intern VL2, but there are still problems in multi-card parallel situations. ``` (VllmWorkerProcess pid=29708) ERROR 09-03 12:08:10 multiproc_worker_utils.py:226] [rank0]: Traceback (most recent call last): [rank0]: File "offline_inference_vision_language.py", line 240, in [rank0]: main(args) [rank0]: File "offline_inference_vision_language.py", line 190, in main [rank0]: llm, prompt, stop_token_ids = model_example_map[model](question) [rank0]: File "offline_inference_vision_language.py", line 135, in run_internvl [rank0]: llm = LLM( [rank0]: File "/home/tdj/intervl/temp_vllm/vllm/vllm/entrypoints/llm.py", line 177, in __init__ [rank0]: self.llm_engine = LLMEngine.from_engine_args( [rank0]: File "/home/tdj/intervl/temp_vllm/vllm/vllm/engine/llm_engine.py", line 541, in from_engine_args [rank0]: engine = cls( [rank0]: File "/home/tdj/intervl/temp_vllm/vllm/vllm/engine/llm...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: InternVL2-26B tensor_parallel_size=4, AssertionError: 25 is not divisible by 4 bug ### Your current environment Python3.8 8*A10 GPU Model:InternVL2-26B vllm branch:main torch
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: py", line 229, in [rank0]: InternVisionEncoderLayer(config=config, quant_config=quant_config) [rank0]: File "/home/tdj/intervl/temp_vllm/vllm/vllm/model_executor/models/intern_vit.py", line 190, in __init__ [rank0]: sel...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: el_loader/loader.py", line 170, in _initialize_model [rank0]: return build_model( [rank0]: File "/home/tdj/intervl/temp_vllm/vllm/vllm/model_executor/model_loader/loader.py", line 155, in build_model [rank0]: return mod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: template(messages, tokenize=False, add_generation_prompt=True) # Stop tokens for InternVL # models variants may have different stop tokens # please refer to the model card for the correct "stop

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
