# vllm-project/vllm#795: "attn_bias is not correctly aligned" on A100 for MPT-30B

| 字段 | 值 |
| --- | --- |
| Issue | [#795](https://github.com/vllm-project/vllm/issues/795) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;frontend_api;model_support;sampling_logits |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 |  |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> "attn_bias is not correctly aligned" on A100 for MPT-30B

### Issue 正文摘录

Hello, I saw a similar issue to this for MPT30B0-chat on H100, but I see the same error on A100 80Gb. Using vllm 0.1.3. Is there any workaround to fix this currently? It does happen for random prompt, so not straightforward to understand where it's coming from: 96 │ │ │ │ prompt_template = PromptTemplate(input_variables=["text"] │ │ 97 │ │ │ │ answer_chain = LLMChain(llm=self.llm , prompt=prompt_temp │ │ 98 │ │ │ │ │ │ ❱ 99 │ │ │ │ response = answer_chain.run(query) │ │ 100 │ │ │ │ │ 101 │ │ │ else: │ │ 102 │ │ │ │ /root/miniconda3/envs/py311/lib/python3.11/site-packages/langchain/chains/base. │ │ py:440 in run │ │ │ │ 437 │ │ if args and not kwargs: │ │ 438 │ │ │ if len(args) != 1: │ │ 439 │ │ │ │ raise ValueError("`run` supports only one positional argu │ │ ❱ 440 │ │ │ return self(args[0], callbacks=callbacks, tags=tags, metadata │ │ 441 │ │ │ │ _output_key │ │ 442 │ │ │ ] │ │ 443 │ │ │ │ /root/miniconda3/envs/py311/lib/python3.11/site-packages/langchain/chains/base. │ │ py:243 in __call__ │ │ │ │ 240 │ │ │ ) │ │ 241 │ │ except (KeyboardInterrupt, Exception) as e: │ │ 242 │ │ │ run_manager.on_chain_error(e) │ │ ❱ 243 │ │ │ raise e │ │ 244 │ │ run_manager.on_chain_end(outputs) │...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: "attn_bias is not correctly aligned" on A100 for MPT-30B bug Hello, I saw a similar issue to this for MPT30B0-chat on H100, but I see the same error on A100 80Gb. Using vllm 0.1.3. Is there any workaround to fix this cu...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: │ │ 101 │ │ │ else: │ │ 102 │ │
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: │ │ ❱ 399 │ │ │ out = xops.memory_efficient_attention_forward( │ │ 400 │ │ │ │ query[None, start:end], │ │ 401 │ │ │ │ key[None, start:end], │ │ 402 │
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: │ │ ❱ 64 │ │ output = model.generate(prompt, sampling_params) │ │ 65 │ │ │ │ 66 │ │ return output[0].outputs[0].text
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: t_token_ids[i] │ │ 129 │ │ │ self._add_request(prompt, sampling_params, token_ids) │ │ ❱ 130 │ │ return self._run_engine(use_tqdm) │ │ 131 │

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
