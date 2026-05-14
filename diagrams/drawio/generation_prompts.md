# draw.io Generation Notes

Use these files with draw.io Mermaid import:

1. Open draw.io.
2. Go to `Arrange > Insert > Advanced > Mermaid`.
3. Paste one `.mmd` file at a time.
4. Generate the diagram, then adjust spacing and export it for the report.

## Files

- `use_case_global.mmd`: global use case diagram for all actors.
- `class_global.mmd`: global class diagram based on the database schema.
- `seq_upload_asset.mmd`: seller upload and admin moderation sequence.
- `seq_purchase_asset.mmd`: cart, payment, order, and library unlock sequence.
- `seq_intern_request.mmd`: intern request, approval, voucher creation, and redemption sequence.

## AI Prompt For draw.io Generate

If you use draw.io's text-to-diagram generation instead of Mermaid import, use this prompt:

Create a clean UML diagram for the IGS Marketplace platform. The system is a digital asset marketplace and internal workspace for Inherited Games Studio. Actors include Visitor, Member, Seller, Intern, Employee, Admin, Super Admin, Payment Provider, AI Service, and Supabase Storage. Core marketplace features are authentication, catalog browsing, asset details and previews, seller uploads, asset moderation, cart, payment, orders, library downloads, reviews, ratings, subscriptions, vouchers, groups, trades, notifications, AI chatbot, review analysis, and recommendations. Internal workspace features include team management, project management, task tracking, project documents, dashboard statistics, and real-time chat. Use clear UML notation, keep relationships readable, and group related functions by marketplace, administration, intern workflow, AI, and workspace.

For class diagrams, base the model on these core entities: User, Role, Permission, Category, Asset, AssetFormat, Order, OrderItem, CartItem, UserDownload, AssetReview, AssetRating, RoleRequest, AssetEditRequest, InternAssetRequest, VoucherCode, SubscriptionPlan, UserSubscription, Group, Trade, Project, WorkspaceTask, ChatChannel, ChatMessage, Notification, AuditLog. Show multiplicities and association names.

For sequence diagrams, generate separate flows for seller asset upload and moderation, member purchase and library unlock, and intern asset request with voucher redemption.
