# vllm-project/vllm#15983: [Bug]: qwen2.5-vl-72b-instruct caused more VRAM in 0.8.0 than 0.7.3

| 字段 | 值 |
| --- | --- |
| Issue | [#15983](https://github.com/vllm-project/vllm/issues/15983) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: qwen2.5-vl-72b-instruct caused more VRAM in 0.8.0 than 0.7.3

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug VLLM_WORKER_MULTIPROC_METHOD=spawn python -m vllm.entrypoints.openai.api_server \ --dtype auto \ --port 8009 \ --trust-remote-code \ --served-model-name qwen2vl \ --model /home/ps/data/pretrained_model/Qwen/Qwen2.5-VL-72B-Instruct/ \ --tensor-parallel-size 4 \ --gpu_memory_utilization 0.95 \ --max_num_seqs 2 \ --max_model_len 8192 \ --mm_processor_kwargs '{"max_pixels":1280, "min_pixels":256}' Use the same start code above, I can successfuly launch qwen2.5-vl-72b-instruct on 4 A100 40G cards and the start is fast. After I update VLLM to 0.8.0, it start very slow with torch.compile, I can see the model is loaded, before it runs graph captures and start, but now it runs torch.compile and raise OOM error. Can anyone help me~~ Thank you very much! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: start code above, I can successfuly launch qwen2.5-vl-72b-instruct on 4 A100 40G cards and the start is fast. After I update VLLM to 0.8.0, it start very slow with torch.compile, I can see the model is loaded, before it...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: qwen2.5-vl-72b-instruct caused more VRAM in 0.8.0 than 0.7.3 bug ### Your current environment ### 🐛 Describe the bug VLLM_WORKER_MULTIPROC_METHOD=spawn python -m vllm.entrypoints.openai.api_server \ --dtype auto...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: art is fast. After I update VLLM to 0.8.0, it start very slow with torch.compile, I can see the model is loaded, before it runs graph captures and start, but now it runs torch.compile and raise OOM error. Can anyone hel...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: _MULTIPROC_METHOD=spawn python -m vllm.entrypoints.openai.api_server \ --dtype auto \ --port 8009 \ --trust-remote-code \ --served-model-name qwen2vl \ --model /home/ps/data/pretrained_model/Qwen/Qwen2.5-VL-72B-Instruct...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: t runs graph captures and start, but now it runs torch.compile and raise OOM error. Can anyone help me~~ Thank you very much! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
