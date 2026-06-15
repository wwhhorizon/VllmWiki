# vllm-project/vllm#12590: [Doc]: apparently missing git clone in "Build wheel from source" non-GPU installation documentation

| 字段 | 值 |
| --- | --- |
| Issue | [#12590](https://github.com/vllm-project/vllm/issues/12590) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: apparently missing git clone in "Build wheel from source" non-GPU installation documentation

### Issue 正文摘录

### 📚 The doc issue I'm trying to follow the OpenVino documentation at https://docs.vllm.ai/en/latest/getting_started/installation/ai_accelerator/index.html and have noticed that there's an implicit git clone of the vllm.git repository, but it's not actually mentioned anywhere. The text "Second, install prerequisites vLLM OpenVINO backend installation:" also seems to be missing a word; is it install prerequisites [for the] vLLM [...]"? This seems to also be the case in other instructions, such as the x86 and ARM build wheel from source instructions here: https://docs.vllm.ai/en/latest/getting_started/installation/cpu/index.html ### Suggest a potential alternative/fix I think it's just missing the git clone line that other methods use. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Doc]: apparently missing git clone in "Build wheel from source" non-GPU installation documentation documentation ### 📚 The doc issue I'm trying to follow the OpenVino documentation at https://docs.vllm.ai/en/latest/get...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ntioned anywhere. The text "Second, install prerequisites vLLM OpenVINO backend installation:" also seems to be missing a word; is it install prerequisites [for the] vLLM [...]"? This seems to also be the case in other...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: trying to follow the OpenVino documentation at https://docs.vllm.ai/en/latest/getting_started/installation/ai_accelerator/index.html and have noticed that there's an implicit git clone of the vllm.git repository, but it...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
