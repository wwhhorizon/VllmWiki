# vllm-project/vllm#37668: Early Stopping for Ouro models

| 字段 | 值 |
| --- | --- |
| Issue | [#37668](https://github.com/vllm-project/vllm/issues/37668) |
| 状态 | open |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Early Stopping for Ouro models

### Issue 正文摘录

### Your current environment Python 3.12.13 vllm 0.17.1 torch 2.10.0+cu129 ### Question Hello, I want to add early exit for "ouro" models ([ouro.py](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/ouro.py)). However I'm not completely sure how model runner is using "hidden_states" from the model. Basically will it break the runner if instead of last hidden states I will return hidden state based on the decoder layer probability? ```python ## ouro.py def forward( self, input_ids: torch.Tensor | None, positions: torch.Tensor, intermediate_tensors: IntermediateTensors | None = None, inputs_embeds: torch.Tensor | None = None, ) -> torch.Tensor | IntermediateTensors: if inputs_embeds is not None: hidden_states = inputs_embeds else: hidden_states = self.embed_input_ids(input_ids) # self.early_exit_threshold = getattr(config, "early_exit_threshold", None) # self.use_early_exit = self.early_exit_threshold is not None and 0 =self.early_exit_threshold)] = False return early_exist_hidden_state ``` ### How would you like to use vllm I want to use vllm to run LoopLM architecture inference ### Before submitting a new issue... - [x] Make sure you already searched for re...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Early Stopping for Ouro models usage ### Your current environment Python 3.12.13 vllm 0.17.1 torch 2.10.0+cu129 ### Question Hello, I want to add early exit for "ouro" models ([ouro.py](https://github.com/vllm-project/v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: `` ### How would you like to use vllm I want to use vllm to run LoopLM architecture inference ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living a...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: s_embeds is not None: hidden_states = inputs_embeds else: hidden_states = self.embed_input_ids(input_ids) # self.early_exit_threshold = getattr(config, "early_exit_threshold", None) # self.use_early_exit = self.early_ex...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: if instead of last hidden states I will return hidden state based on the decoder layer probability? ```python ## ouro.py def forward( self, input_ids: torch.Tensor | None, positions: torch.Tensor, intermediate_tensors:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
