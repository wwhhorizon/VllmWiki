# vllm-project/vllm#43641: [Feature]: Add a route-extension hook to the Rust vllm-server frontend

| 字段 | 值 |
| --- | --- |
| Issue | [#43641](https://github.com/vllm-project/vllm/issues/43641) |
| 状态 | open |
| 标签 | rust |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add a route-extension hook to the Rust vllm-server frontend

### Issue 正文摘录

### Proposal The Rust `vllm-server` frontend currently owns router construction internally: - `rust/src/server/src/lib.rs` calls `build_router(state.clone())` - `rust/src/server/src/routes.rs` defines the fixed OpenAI/vLLM route set Would you be open to exposing a small route-extension hook so Rust integrations can mount additional management endpoints on the same HTTP server without reverse proxying, vendoring, or forking `vllm-server`? One possible API shape: ```rust pub async fn serve_with_routes( config: Config, shutdown: CancellationToken, extra_routes: axum::Router, ) -> anyhow::Result { serve_with_router_extension(config, shutdown, move |router| { router.merge(extra_routes) }).await } pub async fn serve_with_router_extension ( config: Config, shutdown: CancellationToken, extend_router: F, ) -> anyhow::Result where F: FnOnce(axum::Router) -> axum::Router, { // Same implementation as `serve`, except: // let app = extend_router(build_router(state.clone())); } ``` `serve(config, shutdown)` could remain unchanged and delegate to the extension form with an identity closure. ### Motivation The Rust frontend is becoming a useful embeddable frontend layer. Some Rust integrations nee...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: s router construction internally: - `rust/src/server/src/lib.rs` calls `build_router(state.clone())` - `rust/src/server/src/routes.rs` defines the fixed OpenAI/vLLM route set Would you be open to exposing a small route-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: `? One possible API shape: ```rust pub async fn serve_with_routes( config: Config, shutdown: CancellationToken, extra_routes: axum::Router, ) -> anyhow::Result { serve_with_router_extension(config, shutdown, move |route...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: defines the fixed OpenAI/vLLM route set Would you be open to exposing a small route-extension hook so Rust integrations can mount additional management endpoints on the same HTTP server without reverse proxying, vendori...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ontend rust ### Proposal The Rust `vllm-server` frontend currently owns router construction internally: - `rust/src/server/src/lib.rs` calls `build_router(state.clone())` - `rust/src/server/src/routes.rs` defines the fi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
