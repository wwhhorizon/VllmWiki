# vllm-project/vllm#14816: [Usage]: max_model_len, max_num_seqs  and mm_counts

| 字段 | 值 |
| --- | --- |
| Issue | [#14816](https://github.com/vllm-project/vllm/issues/14816) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support;multimodal_vlm |
| 子分类 | install |
| Operator 关键词 | gemm |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: max_model_len, max_num_seqs  and mm_counts

### Issue 正文摘录

### Your current environment When I run VLLM with Qwen in a standard way on a H100: docker run --gpus all \ -v ~/huggingface:/root/.cache/huggingface \ -p 8000:8000 \ --ipc=host \ --name vllm2 \ vllm/vllm-openai:latest \ --model Qwen/Qwen2.5-VL-7B-Instruct \ I typically get some warnings like this: The context length (5120) of the model is too short to hold the multi-modal embeddings in the worst case (32768 tokens in total, out of which {'image': 16384, 'video': 16384} are reserved for multi-modal embeddings). This may cause certain multi-modal inputs to fail during inference, even when the input text is short. To avoid this, you should increase `max_model_len`, reduce `max_num_seqs`, and/or reduce `mm_counts`. Where does the context length of 5120 come from? The init tells me max_seq_len=128000 but I don't see this parameter in the engine arguments (https://docs.vllm.ai/en/latest/serving/engine_args.html). Just max-seq-len-to-capture. Is this the same? Would max_model_len=32768 then fix this problem? How do I set the reserved tokens for MM and text? I also don't see mm_counts as a engine parameters. I have another warning: WARNING 03-13 07:36:00 model_runner.py:1288] Computed ma...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: max_model_len, max_num_seqs and mm_counts usage ### Your current environment When I run VLLM with Qwen in a standard way on a H100: docker run --gpus all \ -v ~/huggingface:/root/.cache/huggingface \ -p 8000:80...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ent environment When I run VLLM with Qwen in a standard way on a H100: docker run --gpus all \ -v ~/huggingface:/root/.cache/huggingface \ -p 8000:8000 \ --ipc=host \ --name vllm2 \ vllm/vllm-openai:latest \ --model Qwe...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Setting it to the minimum value of 1. It looks like you are trying to rescale already rescaled images. If the input images have pixel values between 0 and 1, set `do_rescale=False` to avoid rescaling them again. This al...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ur current environment When I run VLLM with Qwen in a standard way on a H100: docker run --gpus all \ -v ~/huggingface:/root/.cache/huggingface \ -p 8000:8000 \ --ipc=host \ --name vllm2 \ vllm/vllm-openai:latest \ --mo...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: If the input images have pixel values between 0 and 1, set `do_rescale=False` to avoid rescaling them again. This also seems to include the context length of 5120 and 114688 comes suspiciously close to the max_seq_len=1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
