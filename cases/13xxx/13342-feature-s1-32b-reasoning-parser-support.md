# vllm-project/vllm#13342: [Feature]: S1-32B Reasoning Parser support

| 字段 | 值 |
| --- | --- |
| Issue | [#13342](https://github.com/vllm-project/vllm/issues/13342) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: S1-32B Reasoning Parser support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch While S1 recognizes logical structures in legal texts, its reasoning is somewhat unstructured. ### Alternatives this is my code with s1 parser # SPDX-License-Identifier: Apache-2.0 import re from typing import Optional, Sequence, Tuple, Union from transformers import PreTrainedTokenizerBase from vllm.entrypoints.openai.protocol import (ChatCompletionRequest, DeltaMessage) from vllm.entrypoints.openai.reasoning_parsers.abs_reasoning_parsers import ( ReasoningParser, ReasoningParserManager) from vllm.logger import init_logger logger = init_logger(__name__) @ReasoningParserManager.register_module("s1") class S1ReasoningParser(ReasoningParser): """ Reasoning parser for DeepSeek R1 model. The DeepSeek R1 model uses ... tokens to denote reasoning text. This parser extracts the reasoning content from the model output. """ def __init__(self, tokenizer: PreTrainedTokenizerBase): super().__init__(tokenizer) self.think_start_token = "think" self.think_end_token = "answer" escaped_start = re.escape(self.think_start_token) escaped_end = re.escape(self.think_end_token) self.reasoning_regex = re.compile( rf"\b{escaped_start}\b(.*?){escaped_end}\b", re.DOTA...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: s this is my code with s1 parser # SPDX-License-Identifier: Apache-2.0 import re from typing import Optional, Sequence, Tuple, Union from transformers import PreTrainedTokenizerBase from vllm.entrypoints.openai.protocol...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: S1-32B Reasoning Parser support feature request;stale ### 🚀 The feature, motivation and pitch While S1 recognizes logical structures in legal texts, its reasoning is somewhat unstructured. ### Alternatives th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: mpt ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: content, content=content if content else None) elif self.think_end_token_id in previous_token_ids: # think in previous, answer in previous, # reasoning content continues return DeltaMessage(content
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ingParser(ReasoningParser): """ Reasoning parser for DeepSeek R1 model. The DeepSeek R1 model uses ... tokens to denote reasoning text. This parser extracts the reasoning content from the model output. """ def __init__(...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
