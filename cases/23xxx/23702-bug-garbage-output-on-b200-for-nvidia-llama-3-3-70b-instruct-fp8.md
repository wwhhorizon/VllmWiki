# vllm-project/vllm#23702: [Bug]: garbage output on B200 for nvidia/Llama-3.3-70B-Instruct-FP8

| 字段 | 值 |
| --- | --- |
| Issue | [#23702](https://github.com/vllm-project/vllm/issues/23702) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: garbage output on B200 for nvidia/Llama-3.3-70B-Instruct-FP8

### Issue 正文摘录

### Your current environment TODO but this happens on Blackwell with [flashinfer-python==0.2.14.post1](https://github.com/flashinfer-ai/flashinfer/releases/tag/v0.2.14.post1) installed. ### 🐛 Describe the bug This code generates garbage outputs on main: ``` python examples/offline_inference/basic/generate.py --disable-log-stats --no-enable-prefix-caching --load-format=dummy --model nvidia/Llama-3.3-70B-Instruct-FP8 -O.pass_config.enable_attn_fusion=True -O.pass_config.enable_noop=True -O.splitting_ops=[] -O.custom_ops+=+quant_fp8 --kv-cache-dtype fp8 -O.cudagraph_mode=NONE ``` Different (but still garbage outputs) are also present even if fusion is disabled (removing the `-O.pass_config.enable_attn_fusion=True` flag). Note that CUDA Graphs are disabled. I haven't been able to disect the issue to figure out what part is causing the garbage outputs. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: garbage output on B200 for nvidia/Llama-3.3-70B-Instruct-FP8 bug ### Your current environment TODO but this happens on Blackwell with [flashinfer-python==0.2.14.post1](https://github.com/flashinfer-ai/flashinfer/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: garbage output on B200 for nvidia/Llama-3.3-70B-Instruct-FP8 bug ### Your current environment TODO but this happens on Blackwell with [flashinfer-python==0.2.14.post1](https://github.com/flashinfer-ai/flashinfer/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: garbage output on B200 for nvidia/Llama-3.3-70B-Instruct-FP8 bug ### Your current environment TODO but this happens on Blackwell with [flashinfer-python==0.2.14.post1](https://github.com/flashinfer-ai/flashinfer/...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ug ### Your current environment TODO but this happens on Blackwell with [flashinfer-python==0.2.14.post1](https://github.com/flashinfer-ai/flashinfer/releases/tag/v0.2.14.post1) installed. ### 🐛 Describe the bug This co...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: (https://github.com/flashinfer-ai/flashinfer/releases/tag/v0.2.14.post1) installed. ### 🐛 Describe the bug This code generates garbage outputs on main: ``` python examples/offline_inference/basic/generate.py --disable-l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
