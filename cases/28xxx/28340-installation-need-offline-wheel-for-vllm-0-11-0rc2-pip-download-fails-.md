# vllm-project/vllm#28340: [Installation]: Need offline wheel for vLLM 0.11.0rc2 (pip download fails) to deploy qwen3_vl_235b_a22b_instruct_i18n

| 字段 | 值 |
| --- | --- |
| Issue | [#28340](https://github.com/vllm-project/vllm/issues/28340) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Need offline wheel for vLLM 0.11.0rc2 (pip download fails) to deploy qwen3_vl_235b_a22b_instruct_i18n

### Issue 正文摘录

### Your current environment I need to install vLLM 0.11.0rc2 in an offline environment. Is there an official wheel (.whl) available for vLLM==0.11.0rc2 that I can download directly? Running: ``` pip download vllm==0.11.0rc2 --pre --extra-index-url https://wheels.vllm.ai/nightly -d wheels ``` fails with an error: Looking in indexes: https://bytedpypi.byted.org/simple/, https://wheels.vllm.ai/nightly ERROR: Ignored the following yanked versions: 0.2.1 ERROR: Could not find a version that satisfies the requirement vllm==0.11.0rc2 (from versions: 0.0.1, 0.1.0, 0.1.1, 0.1.2, 0.1.3, 0.1.4, 0.1.5, 0.1.6, 0.1.7, 0.2.0, 0.2.1.post1, 0.2.2, 0.2.3, 0.2.4, 0.2.5, 0.2.6, 0.2.7, 0.3.0, 0.3.1, 0.3.2, 0.3.3, 0.4.0, 0.4.0.post1, 0.4.1, 0.4.2, 0.4.3, 0.5.0, 0.5.0.post1, 0.5.1, 0.5.2, 0.5.3, 0.5.3.post1, 0.5.4, 0.5.5, 0.6.0, 0.6.1, 0.6.1.post1, 0.6.1.post2, 0.6.2, 0.6.3, 0.6.3.post1, 0.6.4, 0.6.4.post1, 0.6.5, 0.6.6, 0.6.6.post1, 0.7.0, 0.7.1, 0.7.2, 0.7.3, 0.8.0, 0.8.1, 0.8.2, 0.8.3, 0.8.4, 0.8.5, 0.8.5.post1, 0.9.0, 0.9.0.1, 0.9.1, 0.9.2, 0.10.0, 0.10.1, 0.10.1.1, 0.10.2, 0.11.0, 0.11.1rc6.dev210+g70af44fd1.cu129) ERROR: No matching distribution found for vllm==0.11.0rc2. ### How you are installi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation]: Need offline wheel for vLLM 0.11.0rc2 (pip download fails) to deploy qwen3_vl_235b_a22b_instruct_i18n installation ### Your current environment I need to install vLLM 0.11.0rc2 in an offline environment.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: n]: Need offline wheel for vLLM 0.11.0rc2 (pip download fails) to deploy qwen3_vl_235b_a22b_instruct_i18n installation ### Your current environment I need to install vLLM 0.11.0rc2 in an offline environment. Is there an...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
