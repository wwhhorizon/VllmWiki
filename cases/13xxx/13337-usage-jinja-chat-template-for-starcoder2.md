# vllm-project/vllm#13337: [Usage]: jinja chat template for starcoder2

| 字段 | 值 |
| --- | --- |
| Issue | [#13337](https://github.com/vllm-project/vllm/issues/13337) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: jinja chat template for starcoder2

### Issue 正文摘录

### Your current environment Hi all, I want to use starcoder2 using vllm run on a Docker container. here is my config: ``` --model neuralmagic/starcoder2-7b-quantized.w8a8 \ --disable-log-requests \ --use-v2-block-manager \ --max_num_batched_tokens 32000 \ --block-size 32 \ --max-num-seqs 600" ``` when I start the Docker container, I get this error, but the program continues to run (although it produces nonsense): ``` ERROR 02-15 09:45:26 serving_chat.py:181] Error in preprocessing prompt inputs ERROR 02-15 09:45:26 serving_chat.py:181] Traceback (most recent call last): ERROR 02-15 09:45:26 serving_chat.py:181] File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/serving_chat.py", line 165, in create_chat_completion ERROR 02-15 09:45:26 serving_chat.py:181] ) = await self._preprocess_chat( ERROR 02-15 09:45:26 serving_chat.py:181] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 02-15 09:45:26 serving_chat.py:181] File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/serving_engine.py", line 479, in _preprocess_chat ERROR 02-15 09:45:26 serving_chat.py:181] request_prompt = apply_hf_chat_template( ERROR 02-15 09:45:26 serving_chat.py:181] ^^^^^^^^^^^^^^^^^^^^^^...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: want to use starcoder2 using vllm run on a Docker container. here is my config: ``` --model neuralmagic/starcoder2-7b-quantized.w8a8 \ --disable-log-requests \ --use-v2-block-manager \ --max_num_batched_tokens 32000 \ -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: urrent environment Hi all, I want to use starcoder2 using vllm run on a Docker container. here is my config: ``` --model neuralmagic/starcoder2-7b-quantized.w8a8 \ --disable-log-requests \ --use-v2-block-manager \ --max...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: container. here is my config: ``` --model neuralmagic/starcoder2-7b-quantized.w8a8 \ --disable-log-requests \ --use-v2-block-manager \ --max_num_batched_tokens 32000 \ --block-size 32 \ --max-num-seqs 600" ``` when I st...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rovide a chat template if the tokenizer does not define one. ``` after searching, I found out that I need to define a chat template for the LLM. Can somebody help me to do so? ### How would you like to use vllm I want t...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: starcoder2-7b-quantized.w8a8 \ --disable-log-requests \ --use-v2-block-manager \ --max_num_batched_tokens 32000 \ --block-size 32 \ --max-num-seqs 600" ``` when I start the Docker container, I get this error, but the pr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
