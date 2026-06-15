# vllm-project/vllm#38486: [Bug]: cuda graph takes too much memory for qwen 3.5

| 字段 | 值 |
| --- | --- |
| Issue | [#38486](https://github.com/vllm-project/vllm/issues/38486) |
| 状态 | open |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;fp8;quantization |
| 症状 | build_error;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: cuda graph takes too much memory for qwen 3.5

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi, everything is OK with enforce eager: docker run --runtime nvidia --gpus all -d --name vllm-Qwen35_35B_fp8_v20 --restart unless-stopped -v ~/.cache/huggingface/hub:/models -v ~/.cache/vllm:/root/.cache/vllm -v ~/.cache/huggingface:/root/.cache/huggingface -p 8000:8000 vllm/vllm-openai:v0.18.0 --model Qwen/Qwen3.5-35B-A3B-FP8 --served-model-name llm vllm-local vllm --enforce-eager but generation speed is very slow: 14.43 tokens per second int4 version (Qwen/Qwen3.5-35B-A3B-GPTQ-Int4) gives me: 109.97 tokens per second but with cuda graph but I can't remove enforce-eager flag, because of out of memory. Probably there is problem with cuda graph. from logs: Model loading took 33.38 GiB memory and 21.582860 seconds So after loading weight 33 gb of memory of occupied, but I have 44 gb of memory: from logs: torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 1.03 GiB. GPU 0 has a total capacity of 44.40 GiB of which 858.31 MiB is free. even when max model length is set to 1024: docker run --runtime nvidia --gpus all -d --name vllm-Qwen35_35B_fp8_v23 --restart unless-stopped -v ~/.cache/huggingface/hub:/models -v ~/.cache/vl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: t ### 🐛 Describe the bug Hi, everything is OK with enforce eager: docker run --runtime nvidia --gpus all -d --name vllm-Qwen35_35B_fp8_v20 --restart unless-stopped -v ~/.cache/huggingface/hub:/models -v ~/.cache/vllm:/r...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: eager: docker run --runtime nvidia --gpus all -d --name vllm-Qwen35_35B_fp8_v20 --restart unless-stopped -v ~/.cache/huggingface/hub:/models -v ~/.cache/vllm:/root/.cache/vllm -v ~/.cache/huggingface:/root/.cache/huggin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: cuda graph takes too much memory for qwen 3.5 bug ### Your current environment ### 🐛 Describe the bug Hi, everything is OK with enforce eager: docker run --runtime nvidia --gpus all -d --name vllm-Qwen35_35B_fp8_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: cuda graph takes too much memory for qwen 3.5 bug ### Your current environment ### 🐛 Describe the bug Hi, everything is OK with enforce eager: docker run --runtime nvidia --gpus all -d --name vllm-Qwen35_35B_fp8_v
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: in total (EngineCore pid=86) INFO 03-29 18:34:26 [monitor.py:76] Initial profiling/warmup run took 78.59 s and than: (EngineCore pid=86) ERROR 03-29 18:34:32 [core.py:1099] File "/usr/local/lib/python3.12/dist-packages/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
