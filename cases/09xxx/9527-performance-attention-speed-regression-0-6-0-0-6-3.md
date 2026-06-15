# vllm-project/vllm#9527: [Performance]: attention speed regression 0.6.0 => 0.6.3

| 字段 | 值 |
| --- | --- |
| Issue | [#9527](https://github.com/vllm-project/vllm/issues/9527) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: attention speed regression 0.6.0 => 0.6.3

### Issue 正文摘录

### Report of performance regression I found the attention (flashattn.py) computation time increased 1.7x after upgrade vllm 0.6.0 to 0.6.3. | | v0.6.0 | v0.6.3 | | :----: | :----: | :----: | | attention_cost millisecond (each row is a token decode iteration) | 2.38347053 1.78241729 1.79243087 1.79433822 1.82199478 1.80625915 1.79409980 1.76978111 1.80387496 1.79624557 1.81937217 1.78265571 1.84106826 1.80602073 1.77788734 1.80101394 | 3.56459617 3.22890281 3.22747230 3.11017036 3.15999984 3.00359725 3.14855575 3.08299064 3.09920310 2.99334526 3.05557250 3.21292877 3.29303741 3.24964523 2.98380851 3.11732292 | My test code is as below ```python sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=40) llm = LLM(model="facebook/opt-125m", enforce_eager=True) outputs = llm.generate("Hello, my name is", sampling_params=sampling_params) ``` I modified the `opt.py` to trace the attention computation time ```python attention_cost = 0.0 class OPTAttention(nn.Module): def forward( self, hidden_states: torch.Tensor, kv_cache: torch.Tensor, attn_metadata: AttentionMetadata, ) -> torch.Tensor: qkv, _ = self.qkv_proj(hidden_states) q, k, v = qkv.chunk(chunks=3, dim=-1) t1 =...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Your current environment (if you think it is necessary) ```text PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: TencentOS Linux 3.1 (Core) (x86_64)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: s necessary) ```text PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: TencentOS Linux 3.1 (Core) (x86_64) GCC version: (GCC) 8.4.1 20200928 (Red Hat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: s = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=40) llm = LLM(model="facebook/opt-125m", enforce_eager=True) outputs = llm.generate("Hello, my name is", sampling_params=sampling_params) ``` I modified the `op...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: idden_states: torch.Tensor, kv_cache: torch.Tensor, attn_metadata: AttentionMetadata, ) -> torch.Tensor: qkv, _ = self.qkv_proj(hidden_states) q, k, v = qkv.chunk(chunks=3, dim=-1) t1 = time.time() attn_output = self.at...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: attention speed regression 0.6.0 => 0.6.3 performance;stale ### Report of performance regression I found the attention (flashattn.py) computation time increased 1.7x after upgrade vllm 0.6.0 to 0.6.3. | |...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
