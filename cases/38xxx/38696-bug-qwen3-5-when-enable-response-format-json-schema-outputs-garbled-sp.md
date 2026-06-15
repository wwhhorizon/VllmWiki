# vllm-project/vllm#38696: [Bug]: qwen3.5 when enable response_format json_schema outputs garbled spaces

| 字段 | 值 |
| --- | --- |
| Issue | [#38696](https://github.com/vllm-project/vllm/issues/38696) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: qwen3.5 when enable response_format json_schema outputs garbled spaces

### Issue 正文摘录

### Your current environment **Environment** **Use vllm docker images :** vllm/vllm-openai:nightly ,the image id is db683b1d4dce and the create time is 2026-03-27 **Service startup command** vllm serve --model /data/deploy/Qwen3.5-9B/Qwen3.5-9B --enable-auto-tool-choice --tool-call-parser qwen3_coder --reasoning-parser qwen3 --served-model-name qwen3.5-9b-test --tensor-parallel-size 1 --gpu-memory-utilization 0.9 --max-model-len 32768 --limit-mm-per-prompt \{\"image\":12\} ### 🐛 Describe the bug **Prompt** curl --location 'http://127.0.0.1:8000/v1/chat/completions' \ --header 'Content-Type: application/json' \ --data '{ "messages": [ { "role": "system", "content": "## 场景与角色\n\n这是一个AI监控场景。首先摄像头需要绑定CV算法（亦称“能力”）以进行事件检测，然后当事件发生时则会产生相应的告警。摄像头有名称、属地或属主，例如“xx摄像头”、“xx监控”、“银泰城的监控”。根据检测的内容，能力有相关的命名，如：人员入侵检测、烟火烟雾检测、占道经营检测等。事件发生时所产生的告警随之也有相应的类型名称，如：人员入侵、烟火烟雾等，同时事件还有时间、区域、所属摄像头、严重程度等属性。围绕AI监控场景，用户可能需要为摄像头绑定某种能力以进行事件检测，也可能需要查看某摄像头画面以了解当前情况，或者需要查看一些告警的详情，又或者需要对告警做统计分析。你负责结合对话上下文将当前用户输入分类到一个恰当的类别，并对该输入做必要改写使之能够独立完整明确地表达用户意图，以辅助下一步处理。具体地，分类如下：\n\n- 1代表事件统计分析，当用户目的是统计分析告警事件的数量、分布、趋势等情况时，属于此类。例如：“今天发生多少起xx事件”、“查询本周告警按地区（或类型）的分布情况”、“本月xx类事件的趋势”。\n- 2代表事件详情查询，当用户目的是查看告警事件的详情时，属于此类。例如：“查询今日的人员入侵”、“本周有哪...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: qwen3.5 when enable response_format json_schema outputs garbled spaces bug ### Your current environment **Environment** **Use vllm docker images :** vllm/vllm-openai:nightly ,the image id is db683b1d4d
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: d spaces bug ### Your current environment **Environment** **Use vllm docker images :** vllm/vllm-openai:nightly ,the image id is db683b1d4dce and the create time is 2026-03-27 **Service startup command** vllm serve --mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: hed ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: "model": "qwen3.5-9b-test", "max_tokens": 1000, "stream": false, "temperature": 0.1, "top_p": 0.95, "presence_penalty": 1.05, "response_format": { "type": "json_schema", "json_schema": { "name": "rewritingQuestion", "sc...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: rser qwen3_coder --reasoning-parser qwen3 --served-model-name qwen3.5-9b-test --tensor-parallel-size 1 --gpu-memory-utilization 0.9 --max-model-len 32768 --limit-mm-per-prompt \{\"image\":12\} ### 🐛 Describe the bug **P...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
