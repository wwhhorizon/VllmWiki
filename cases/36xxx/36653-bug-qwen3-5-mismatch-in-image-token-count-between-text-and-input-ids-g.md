# vllm-project/vllm#36653: [Bug]: qwen3.5 Mismatch in `image` token count between text and `input_ids`. Got ids=[4091]

| 字段 | 值 |
| --- | --- |
| Issue | [#36653](https://github.com/vllm-project/vllm/issues/36653) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: qwen3.5 Mismatch in `image` token count between text and `input_ids`. Got ids=[4091]

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when running `Sehyo/Qwen3.5-122B-A10B-NVFP4` I am unable to send more than 4091 MM tokens to the model in one request I managed to fix this when sending only one image with `--mm-processor-kwargs '{"min_pixels": 200704, "max_pixels": 614656}'` however this does not work when sending multiple images when sending large payload including 10+ images I am getting: ``` (APIServer pid=1) ERROR 03-10 13:23:29 [serving.py:311] Error in preprocessing prompt inputs (APIServer pid=1) ERROR 03-10 13:23:29 [serving.py:311] Traceback (most recent call last): (APIServer pid=1) ERROR 03-10 13:23:29 [serving.py:311] File "/usr/local/lib/python3.12/dist-packages/vllm/multimodal/processing/context.py", line 267, in call_hf_processor (APIServer pid=1) ERROR 03-10 13:23:29 [serving.py:311] output = hf_processor(**data, **allowed_kwargs, return_tensors="pt") (APIServer pid=1) ERROR 03-10 13:23:29 [serving.py:311] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (APIServer pid=1) ERROR 03-10 13:23:29 [serving.py:311] File "/usr/local/lib/python3.12/dist-packages/transformers/models/qwen3_vl/processing_qwen3_vl.py", line 239, in __call__ (APIS...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: qwen3.5 Mismatch in `image` token count between text and `input_ids`. Got ids=[4091] bug ### Your current environment ### 🐛 Describe the bug when running `Sehyo/Qwen3.5-122B-A10B-NVFP4` I am unable to send more t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: onment ### 🐛 Describe the bug when running `Sehyo/Qwen3.5-122B-A10B-NVFP4` I am unable to send more than 4091 MM tokens to the model in one request I managed to fix this when sending only one image with `--mm-processor-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: qwen3.5 Mismatch in `image` token count between text and `input_ids`. Got ids=[4091] bug ### Your current environment ### 🐛 Describe the bug when running `Sehyo/Qwen3.5-122B-A10B-NVFP4` I am unable to send more t...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: qwen3.5 Mismatch in `image` token count between text and `input_ids`. Got ids=[4091] bug ### Your current environment ### 🐛 Describe the bug when running `Sehyo/Qwen3.5-122B-A10B-NVFP4` I am unable to send more t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: PIServer pid=1) ERROR 03-10 13:23:29 [serving.py:311] self._check_special_mm_tokens(text, text_inputs, modalities=["image", "video"]) (APIServer pid=1) ERROR 03-10 13:23:29 [serving.py:311] File "/usr/local/lib/python3....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
